import os
import hashlib
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
from pipeline import BlogChatbotPipeline
import time

## Load OpenAI and Pinecone Keys

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

INDEX_NAME = "blog-embeddings-v2"

## Create pinecone index (if not already created)

if INDEX_NAME not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(INDEX_NAME)
print("Index ready")

## Build dataframe 

pipeline = BlogChatbotPipeline(
    github_user="simrenbasra",
    repo="simys-blog",
    branch="main",
    post_paths=["about_me.md", "my_projects.md", "_posts"],
    embedding_model="text-embedding-3-small",
    max_length=512
)

df = pipeline.build_dataframe()
df["ingestion_version"] = time.strftime("%Y-%m-%d_%H-%M-%S")

df.to_parquet("chunks.parquet")

print(f"Chunks created: {len(df)}")

# -------------------------
# INGEST
# -------------------------
for i, row in df.iterrows():

    vector_id = hashlib.sha256(
        (row["source"] + "::" + row["chunk_text"]).encode("utf-8")
    ).hexdigest()

    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=row["chunk_text"]
    ).data[0].embedding
    
    index.upsert(
        vectors=[
            {
                "id": vector_id,
                "values": embedding,
                "metadata": {
                    "chunk_text": row["chunk_text"],
                    "post_title": row["post_title"],
                    "date": row["date"],
                    "source": row["source"],
                    "chunk_index": int(row["chunk_index"]) 
                }
            }
        ]
    )

    print(f"Upserted: {row['post_title']} - chunk {i}")

print("INGESTION DONE")
