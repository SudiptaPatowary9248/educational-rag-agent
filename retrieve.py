from sentence_transformers import SentenceTransformer
import chromadb

from config import (
    EMBEDDING_MODEL,
    VECTOR_DB_PATH,
    COLLECTION_NAME,
    TOP_K
)

# trying lazy loading to test Render
embedding_model = None
collection = None

def initialize():

    global embedding_model
    global collection

    if embedding_model is None:

        print("Loading embedding model...")

        embedding_model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    if collection is None:

        print("Loading ChromaDB collection...")

        client = chromadb.PersistentClient(
            path=VECTOR_DB_PATH
        )

        collection = client.get_collection(
            name=COLLECTION_NAME
        )

# embedding_model = SentenceTransformer(
#     EMBEDDING_MODEL
# )
#
# client = chromadb.PersistentClient(
#     path=VECTOR_DB_PATH
# )
#
# collection = client.get_collection(
#     name=COLLECTION_NAME
# )

def retrieve_chunks(query):
    initialize()
    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K,
        include=["documents", "distances"]
    )

    return results
