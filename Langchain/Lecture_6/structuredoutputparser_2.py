# google/gemma-2-2b-it

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#from langchain.output_parsers import StructuredOutputParser, ResponseSchema -> this is not working
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    #max_new_tokens=256,
)

model = ChatHuggingFace(llm = llm)

# creating schema
schema = [
    ResponseSchema(name = 'fact_1', description = 'Fact 1 about the topic'),
    ResponseSchema(name = 'fact_2', description = 'Fact 1 about the topic'),
    ResponseSchema(name = 'fact_3', description = 'Fact 1 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = "give 3 fact about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
