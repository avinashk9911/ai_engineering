# This file deletes one stored document by its Chroma id.
# Run add_documents.py first, then view_documents.py, and copy an id from that output.
#
# Steps:
# 1. Load the same embedding model used when the documents were saved.
# 2. Open the existing "sample" collection in my_chroma_db.
# 3. Delete the row with the given id.
# 4. Print the collection so you can confirm that row is gone.

from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Step 1: open the collection with the same embedding setup used to create it.
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: connect to the database. This file does not add documents.
vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory=str(Path(__file__).parent / "my_chroma_db"),
)

# Step 3: delete uses the id Chroma assigned, not the player name.
# This id came from an earlier run. If it is not in your database, replace it with an id from view_documents.py.
vector_store.delete(ids=["09a39dc6-3ba6-4ea7-927e-fdda591da5e4"])

# Step 4: the deleted document should no longer appear in this print.
print(vector_store.get(include=["embeddings", "documents", "metadatas"]))
