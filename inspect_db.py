import chromadb

client = chromadb.PersistentClient(
    path="vectordb"
)

collection = client.get_collection(
    name="knowledge_base"
)

# updated because .get() by default does not display embeddings
# data = collection.get()
data = collection.get(
    include=["documents", "embeddings"]
)

print(data)
