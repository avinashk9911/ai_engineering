from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda

load_dotenv()

#normal python function
def word_count(word):
    return len(word.split())

llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Llama-3.2-1B-Instruct',
    task= 'conversational',
    provider = 'featherless-ai'
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template = 'Write a jock on {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()


jock_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {'jock' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count)}
    # or we can directly pass the function to RunnableLambda i.e. RunnableLambda(lambda x: len(x.split()))
)

final_chain = RunnableSequence(jock_gen_chain, parallel_chain)
result = final_chain.invoke({'topic':'AI'})
print(result)

# printing in a better way
final_result = """ {} \n count - {}""".format(result['joke'], result['word_count'])
print(final_result)