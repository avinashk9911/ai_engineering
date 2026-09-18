# this code is an example of how we can access a hugging face model - google/gemma-2-2b-it.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    max_new_tokens=256,
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("what is Machine Learining")
print(result.content)