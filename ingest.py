from sentence_transformers import SentenceTransformer
import chromadb

# load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# initialize chromadb client
client = chromadb.PersistentClient(
    path="vectordb"
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)

# read document
with open("data/ml_basics.txt", "r", encoding="utf-8") as f:
    text = f.read()

# simple chunking
chunks = text.split("\n\n")

# create embeddings + store
for idx, chunk in enumerate(chunks):

    embedding = embedding_model.encode(chunk).tolist()

    collection.add(
        documents=[chunk],
        embeddings=[embedding],
        ids=[str(idx)]
    )

print("Ingestion complete.")
