# This file does the same meaning search as similarity_search.py, and also shows how close each match is.
# Run add_documents.py first.
#
# Steps:
# 1. Load the same embedding model used when the documents were saved.
# 2. Open the existing "sample" collection in my_chroma_db.
# 3. Embed the question and return the 2 closest documents with a distance score.
# 4. Print each document together with its score.

from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Step 1: the query must be embedded with the same model as the stored documents.
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: connect to the database. Nothing is added or deleted here.
vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory=str(Path(__file__).parent / "my_chroma_db"),
)

# Step 3: each item in the result is a pair: (Document, score). A smaller score means a closer match.
result = vector_store.similarity_search_with_score(
    query="Who among these are a bowler?",
    k=2,
)

# Step 4: compare the scores to see which player note is closer to the question.
print(result)
