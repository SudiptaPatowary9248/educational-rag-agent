from sentence_transformers import SentenceTransformer
import chromadb

from config import (
    EMBEDDING_MODEL,
    VECTOR_DB_PATH,
    COLLECTION_NAME,
    TOP_K
)

embedding_model = SentenceTransformer(
    EMBEDDING_MODEL
)

client = chromadb.PersistentClient(
    path=VECTOR_DB_PATH
)

collection = client.get_collection(
    name=COLLECTION_NAME
)

def retrieve_chunks(query):
    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K,
        include=["documents", "distances"]
    )

    return results
