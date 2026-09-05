# this code shows how to use the HuggingFace embeddings model to embed a list of documents and get the embedding vectors.

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = ["Delhi is the capital of India", 
             "Mumbai is the financial capital of India", 
             "Bangalore is the IT hub of India"]

vector = embedding.embed_documents(documents)

print(str(vector))