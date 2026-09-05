from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3.6-27b",
    temperature=0,
)

response = llm.invoke(
    "What is the capital of India?"
)

print(response.content)