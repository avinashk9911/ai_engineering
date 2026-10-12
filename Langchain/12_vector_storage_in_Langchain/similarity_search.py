# This file searches the stored player notes by meaning.
# Run add_documents.py first.
#
# Steps:
# 1. Load the same embedding model used when the documents were saved.
# 2. Open the existing "sample" collection in my_chroma_db.
# 3. Embed the question and return the 2 closest documents.
# 4. Print those documents.

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

# Step 3: k=2 means "give me the 2 nearest matches." The result is a list of Document objects, with no score.
result = vector_store.similarity_search(
    query="Who among these are a bowler?",
    k=2,
)

# Step 4: the closest document is first.
print(result)
