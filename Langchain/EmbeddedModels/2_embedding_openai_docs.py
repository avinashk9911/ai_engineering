# this code shows how to use the OpenAI embeddings model to embed a list of documents and get the embedding vectors.

form langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions = 32)

documents = ["Delhi is the capital of India", 
             "Mumbai is the financial capital of India", 
             "Bangalore is the IT hub of India"]

result = embedding.embed_documents(documents)

print(str(result))
