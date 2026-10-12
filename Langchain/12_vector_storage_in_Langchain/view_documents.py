# This file only reads what is already stored in Chroma.
# Run add_documents.py first, otherwise the collection is empty.
#
# Steps:
# 1. Load the same embedding model used when the documents were saved.
# 2. Open the existing "sample" collection in my_chroma_db.
# 3. Print every stored id, document, embedding, and metadata.

from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Step 1: the model is needed so Chroma can open the collection with the same embedding setup.
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: this does not add new documents. It connects to the database created by add_documents.py.
vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory=str(Path(__file__).parent / "my_chroma_db"),
)

# Step 3: get() returns the raw rows. "ids" are always included. The include list adds the other fields.
print(vector_store.get(include=["embeddings", "documents", "metadatas"]))
