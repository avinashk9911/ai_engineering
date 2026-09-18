# this code has been developed using chains

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    #max_new_tokens=256,
)

model = ChatHuggingFace(llm = llm)

#schema
class Person(BaseModel):

    name : str = Field(description= "Name of the person")
    age : int = Field(gt = 18, description = 'Age of the person')
    city : str = Field(description = 'Name of the cidtyy the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables = ['place'],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'place':'India'})
print(result)