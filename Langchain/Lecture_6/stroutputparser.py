# the agenda for this code is to learn String output parser
# hear 1st we will get detailed output form the llm and then use the same output and ask the llm to summarize it

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    max_new_tokens=256,
)

model = ChatHuggingFace(llm = llm)

# 1st prompt -> detailed report

template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summry

template2 = PromptTemplate(
    template = 'Write a 5 line summar on the following text. /n {text}',
    input_variables=['topic']
)

prompt1 = template1.invoke({'topic': 'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke(result.content)

result1 = model.invoke(prompt2)

print(result1.content)