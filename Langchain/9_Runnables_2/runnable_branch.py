# in this code we will learn about RunnableBranch with an expample
# example-
#                                    ->  if words >500 -> again send it to llm for sumarize
#                                   |    
# topic -> prompt -> llm -> parser -
#                                   |
#                                   -> if words <500 -> print


from google.auth import default
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda

load_dotenv()

# prompt to generate report
prompt1 = PromptTemplate(
    template = 'Write a detailed repoirt on {topic}',
    input_variables= ['topic']
)

# prompt if the words in report are more then 500 words
prompt2 = PromptTemplate(
    template = 'Summarize the following text {text}',
    input_variables= ['template']
)


llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Llama-3.2-1B-Instruct',
    task= 'conversational',
    provider = 'featherless-ai'
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

# 1) to create topic -> prompt -> llm -> parser
report_generation_chain = RunnableSequence(prompt1, model, parser)

# now we will create the chain for branch
# RunnableBranch takes tuples -> each condition will have there own tuple.
# each touple will have two inputs 1) condition 2) runnables
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, RunnableSequence(prompt2, model, parser)),
    # we will be receiving a output form report_generation_chain. Now, we are creating a lambda fx and the x will store the result of report_generation_cahin. we will check if the x is grater then 500 then we run RunnableSequence with sencond prompt to summarize
    RunnablePassthrough()
)

final_cahin = RunnableSequence(report_generation_chain, branch_chain)
result = final_cahin.invoke({'topic': 'Russia vs Ukraine'})
print(result)
