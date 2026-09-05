# this code is to show how to use the OpenAI embeddings model to embed a query and get the embedding vector.

form langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "tsext-embedding-3-large", dimensions = 32)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))
