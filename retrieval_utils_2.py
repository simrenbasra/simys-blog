from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
import os
import re
import ast
from openai import OpenAI
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

pc = Pinecone(PINECONE_API_KEY)
client = OpenAI(api_key=OPENAI_API_KEY)

class KeywordSearch:
    """ 
    Returns the most relevant chunks based on keyword matching using TF-IDF vectorisation and cosine similarity.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialises the KeywordSearch class by vectorising the chunks in the provided DataFrame using TF-IDF.
        """
        self.df = df
        self.vectoriser, self.tfidf_matrix, self.metadata_df = self._vectorise_chunks_with_tfidf(df)

    def _preprocess_text(self, text:str) -> str:
        """
        Preprocess text before vectorisation by removing whitespace and non-ASCII characters.
        """
        text = re.sub(r'\s+', ' ', text).strip()
        
        return re.sub(r'[^\x00-\x7F]+', '', text)
    
    def _vectorise_chunks_with_tfidf(self, df: pd.DataFrame) -> tuple:
        """
        Vectorises the chunks in the dataframe using TF-IDF and returns the vectoriser, TF-IDF matrix and dataframe of metadata.    
        """
        vectoriser = TfidfVectorizer(ngram_range=(1,2), stop_words="english",lowercase=True)

        chunk_texts = []
        metadata = []

        for _, row in df.iterrows():
            processed_chunk = self._preprocess_text(row["chunk_text"])
            chunk_texts.append(processed_chunk)

            metadata.append({
                "post_title": row["post_title"],
                "date": str(row["date"]),
                "source": row["source"],
                "chunk_title": row["chunk_title"],
                "chunk_index": row["chunk_index"],
                "chunk_text": row["chunk_text"]
            })

        # reset to ensure index matches the order of the tfidf matrix rows
        metadata_df = pd.DataFrame(metadata).reset_index(drop=True)
        tfidf_matrix = vectoriser.fit_transform(chunk_texts)

        return vectoriser, tfidf_matrix, metadata_df
    
    def retrieve(self, prompt: str, top_k: int = 5) -> list:   
        """
        Returns the most relevant chunks based on keyword matching using TF-IDF vectorisation and cosine similarity. 
        Each result itemb includes the chunk index, chunk title, chunk text, post title, date, source and keyword score.
        """
        processed_prompt = self._preprocess_text(prompt)
        vectorised_prompt = self.vectoriser.transform([processed_prompt])
        scores = cosine_similarity(vectorised_prompt, self.tfidf_matrix)[0]
        top_results = np.argsort(scores)[::-1][:top_k]

        results = []
        
        for i in top_results:

            row = self.metadata_df.iloc[i]

            results.append({
                "chunk_index": int(row["chunk_index"]),
                "chunk_title": row["chunk_title"],
                "chunk_text": row["chunk_text"],
                "post_title": row["post_title"],
                "date": row["date"],
                "source": row["source"],
                "keyword_score": float(scores[i])
            })

        return results
    
class VectorSearch:
    """ 
    Returns the most relevant chunks based on vector similarity using Pinecone vector database.
    Also incorporates a recency score based on the age of the post, which can alter the vector similarity score using the alpha parameter. 
        (i.e. more recent mosts are given higher scores).
    """
    def __init__(self,index_name:str):
        """
        Initialises the VectorSearch class by connecting to Pinecone index (vector db).
        """
        self.index = pc.Index(index_name)

    def clean_date(self, raw_date):
        """
        Converts raw date metadata into a valid datetime object.
        Falls back to current date if the value is missing or invalid.
        """
        current_date = datetime.now()

        try:
            if pd.isna(raw_date) or not raw_date:
                return current_date
            return datetime.fromisoformat(str(raw_date))
        except ValueError:
            return current_date

    def recency_score(self, post_date:str) -> float:
        """
        Calculates a recency score based on the age of the post. 
        More recent posts receive higher scores.
        """
        current_date = datetime.now()
        
        # calculate days old and return recency score (more recent posts get higher scores)
        days_old = (current_date - post_date).days
        return 1 / (1 + days_old)

    def combine_vector_score_with_regency(self,vector_score, post_date, alpha=1.0):
        """
        Combines the vector similarity score with the recency score.
        """
        recency = self.recency_score(post_date)
        return alpha * vector_score + (1 - alpha) * recency

    def retrieve(self, prompt, top_k=5, alpha=1.0):
        """
        Returns the most relevant chunks based on vector similarity using Pinecone vector database.
        When alpha = 1.0 only vector similarity is considered, when alpha = 0.0 only recency is considered.
        """
    
        embedded_prompt = client.embeddings.create(
            model="text-embedding-3-small",
            input=prompt
        ).data[0].embedding

        results = self.index.query(
            vector=embedded_prompt,
            top_k=top_k*3, 
            include_metadata=True
        )

        scored_results = []
        for match in results['matches']:
            metadata = match['metadata']
            
            date = self.clean_date(metadata.get("date"))

            score = self.combine_vector_score_with_regency(match['score'], date, alpha)
            scored_results.append({
                "chunk_index": metadata["chunk_index"],
                "chunk_text": metadata["chunk_text"],
                "chunk_title": metadata["chunk_title"],
                "post_title": metadata["post_title"],
                "date": metadata["date"],
                "source": metadata["source"],
                "score": score,
            })

        scored_results = sorted(scored_results, key=lambda x: x['score'], reverse=True)
        return scored_results[:top_k]

