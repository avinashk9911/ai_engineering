# This file searches only inside one team, using the metadata saved with each document.
# Run add_documents.py first.
#
# Steps:
# 1. Load the same embedding model used when the documents were saved.
# 2. Open the existing "sample" collection in my_chroma_db.
# 3. Keep only documents whose metadata team is "Chennai Super Kings".
# 4. Print those documents with their scores.

from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Step 1: the filter still runs through the embedding model, even when the query text is empty.
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: connect to the database. Nothing is added or deleted here.
vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory=str(Path(__file__).parent / "my_chroma_db"),
)

# Step 3: filter uses the metadata field "team". The empty query means we are not looking for particular words.
result = vector_store.similarity_search_with_score(
    query="",
    filter={"team": "Chennai Super Kings"},
)

# Step 4: Dhoni and Jadeja are the two Chennai Super Kings notes.
print(result)
