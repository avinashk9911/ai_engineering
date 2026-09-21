from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Llama-3.2-1B-Instruct',
    task= 'conversational',
    provider = 'featherless-ai'
)

model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template = 'Write a jock on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain me the following jock {text}',
    input_variables= ['text']
)

parser = StrOutputParser()

jock_generater_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'jock':RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2, model, parser)
    })

final_chain = RunnableSequence(jock_generater_chain,parallel_chain)
result = final_chain.invoke({'topic':'AI'})
print(result)

