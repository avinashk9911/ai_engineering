# This file stores the IPL player notes in Chroma.
# Run this first. The other files in this folder read the same database.
#
# Steps:
# 1. Load a local Hugging Face embedding model.
# 2. Turn each player note into a LangChain Document, with the team saved as metadata.
# 3. Open (or create) the Chroma database in my_chroma_db, next to this file.
# 4. Embed the documents and add them to the "sample" collection.
# 5. Print what was stored, so you can see the text and metadata.

from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

# Step 1: this model turns text into vectors. Chroma uses those vectors for search.
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: page_content is the text that gets embedded. metadata is extra information you can filter on later.
doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"},
)
doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"},
)
doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"},
)
doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"},
)
doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"},
)

docs = [doc1, doc2, doc3, doc4, doc5]

# Step 3: persist_directory keeps the database on disk in this folder, not in the project root.
vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory=str(Path(__file__).parent / "my_chroma_db"),
)

# Step 4: add_documents embeds each document and saves it. Chroma assigns an id to every row.
vector_store.add_documents(docs)

# Step 5: read the collection back. Embeddings are left out here so the print stays readable.
print(vector_store.get(include=["documents", "metadatas"]))
