# this cdoe shows how to use the HuggingFace embeddings model to embed a query and get the embedding vector.

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India"

vector = embedding.embed_query(text)
    
print(str(vector))