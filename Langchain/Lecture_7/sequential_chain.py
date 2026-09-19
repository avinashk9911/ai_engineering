# this is a little bit advanced version of chain
# in this code we will do -> take a prompt form user -> pass that prompt to llm and get detailed output -> get response -> pass that response again to LLM and for this time to create summary
# so first we will create a detailed report, then use that report to generate a summary

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#prompts
prompt1 = PromptTemplate(
    template= "Generate a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summry for the following text \n {text}',
    input_variables= ['text']
)

#model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    max_new_tokens=256,
)

model = ChatHuggingFace(llm = llm)

#parser
parser = StrOutputParser()

#chain
chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'Cricket'})

print(result)

# to visualize the chain working
chain.get_graph().print_ascii()