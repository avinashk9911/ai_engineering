import os
from pathlib import Path

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load .env from the project root (parent of ChatModels/), not from cwd.
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# LangChain/HF look for HUGGINGFACEHUB_API_TOKEN or HF_TOKEN.
# This project stores the token as HUGGINGFACE_API_KEY in .env.
hf_token = (
    os.getenv("HUGGINGFACEHUB_API_TOKEN")
    or os.getenv("HF_TOKEN")
    or os.getenv("HUGGINGFACE_API_KEY")
)

if not hf_token:
    raise ValueError(
        "No Hugging Face token found. Add HUGGINGFACE_API_KEY (or HF_TOKEN) to .env"
    )

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is prime minister of india?")

print(result.content)
