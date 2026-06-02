import os
import hashlib
from openai import OpenAI
from pinecone import Pinecone
from pipeline import BlogChatbotPipeline

# -------------------------
# CLIENTS
# -------------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

INDEX_NAME = "blog-embeddings-v2"

pc.create_index(
    name=INDEX_NAME,
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

print("Index reset complete")
# -------------------------
# PIPELINE
# -------------------------
pipeline = BlogChatbotPipeline(
    github_user="simrenbasra",
    repo="simys-blog",
    branch="main",
    post_paths=["about_me.md", "my_projects.md", "_posts"],
    embedding_model="text-embedding-3-small",
    max_length=512
)

df = pipeline.build_dataframe()
print(f"Chunks created: {len(df)}")

# -------------------------
# INGEST
# -------------------------
for i, row in df.iterrows():

    vector_id = hashlib.md5(
        (row["post_title"] + row["chunk_text"]).encode("utf-8")
    ).hexdigest()

    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=row["chunk_text"]
    ).data[0].embedding

    index.upsert([
        (
            vector_id,
            embedding,
            {
                "chunk_text": row["chunk_text"],
                "post_title": row["post_title"],
                "date": row["date"]
            }
        )
    ])

    print(f"Upserted: {row['post_title']} - chunk {i}")

print("✅ INGESTION COMPLETE")
