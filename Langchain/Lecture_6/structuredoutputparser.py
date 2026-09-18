from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#from langchain.output_parsers import StructuredOutputParser, ResponseSchema -> this is not working
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
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

prompt = template.invoke({'topic':'black hole'})

result = model.invoke(prompt)

print("RAW MODEL OUTPUT:")
print(result.content) # this is giving output in a list fomat i.e. [{'fact_1' : '', 'fact_2':''}], becasue -TinyLlama often wraps answers in a list when you ask for “3 facts.” 
print("---")

final_result = parser.parse(result.content) # it is getting faild because it is return a json raped in a array.
# to fix the issue we need to improve the prompt that we are passing - 
# template = ("Give 3 facts about {topic}.\n Return a single JSON object (not an array) with keys fact_1, fact_2, fact_3.\n {format_instruction}")

print(final_result)