# hear we are learing about jsonoutputparser with the help of parser
# before complting this you shold go through jsonoutputparser.py

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    max_new_tokens=256,
)

model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template = "Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables = [],
    partial_variables= {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# insted of writing all the above code we can simply use chains
chain = template | model | parser
result = chain.invoke({})

print(result)

