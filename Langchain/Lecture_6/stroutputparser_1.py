# in this code we are learning how to use strOutputParser (string output parser) to generate structured output
# strOutputParser genertes output in the form of String.
# we can compare this code and stroutputparser.py file to see how the string parser is different form normal string output.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


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

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser 
# we are forming a cahin i.e.
# we will take our template1 -> pass that to model -> model will give output but form entire output we only need content and to filter that we will use parser
# -> then we will use that output content and make second template i.e template2 -> pass that template to model again for summarize
# -> again the model will generate output but in that out put we only need content and to extract that content we will use parser

#hear by the help of parser we can directly use the output of first template1 model into second template2 model 


result = chain.invoke({'topic':'black hole'})
print(result)