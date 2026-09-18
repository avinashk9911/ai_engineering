# this is one way - without chain. Recomended you use chain jsonoutputparser_1.py

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

prompt = template.format()

# print(prompt) # if we want to see the input prompt

# if you see the output -
# Give me the name, age and city of a fictional person 
#  Return a JSON object.
# hear we can clearly see that the the fomat_instruciton has clearly mantion - return a Json object. and this came form - parser.get_format_instructions()
# the name is 'partial_variables' because the formate has already been filled or defined even before the runtime with the help of 'parser.get_format_instructions()' call

result = model.invoke(prompt)
# print(result)

final_result = parser.parse(result.content)
print(final_result)
# print(final_result['city'])
print(type(final_result))

