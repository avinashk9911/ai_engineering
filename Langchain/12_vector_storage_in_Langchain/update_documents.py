# This file replaces the stored Virat Kohli note with a longer version.
# Run add_documents.py first. Chroma keeps the same id and replaces the text and embedding.
#
# Steps:
# 1. Load the same embedding model used when the documents were saved.
# 2. Open the existing "sample" collection in my_chroma_db.
# 3. Write the new Kohli document.
# 4. Find the id of the current Kohli row. Chroma created that id when the row was added.
# 5. Update that row, then print the collection so you can see the new text.

from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

# Step 1: the replacement text has to be embedded with the same model.
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: connect to the database created by add_documents.py.
vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory=str(Path(__file__).parent / "my_chroma_db"),
)

# Step 3: this is the new text and metadata that will replace the old Kohli note.
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"},
)

# Step 4: update_documents needs the existing id. Look it up from the text instead of hardcoding it.
stored = vector_store.get(include=["documents"])
kohli_ids = [
    doc_id
    for doc_id, content in zip(stored["ids"], stored["documents"])
    if content.startswith("Virat Kohli")
]

# Step 5: update the first matching row, then show the collection after the change.
if kohli_ids:
    vector_store.update_documents(ids=[kohli_ids[0]], documents=[updated_doc1])

print(vector_store.get(include=["embeddings", "documents", "metadatas"]))
