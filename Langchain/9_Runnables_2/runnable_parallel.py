from joblib import parallel
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence


load_dotenv()

#model1
llm1 = HuggingFaceEndpoint(
    repo_id= 'meta-llama/Llama-3.2-1B-Instruct',
    task = 'converersational',
    provider="featherless-ai"
)

model1 = ChatHuggingFace(llm = llm1)

llm2 = HuggingFaceEndpoint(
    repo_id = 'google/gemma-2-2b-it',
    task = 'conversational',
    provider = 'featherless-ai'
)

model2 = ChatHuggingFace(llm = llm2)

prompt1 = PromptTemplate(
    template = 'Write me a linkedin post about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Write me a tweet about {topic}',
    input_variables= ['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'linkedin': RunnableSequence(prompt1, model1, parser),
    'tweet' : RunnableSequence(prompt2, model2, parser)  # on both the RunnableSequence we can use same model
})

result= parallel_chain.invoke({'topic':'AI'})
print(result)