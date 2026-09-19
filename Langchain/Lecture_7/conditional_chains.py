# in this code we will learn about conditional chains
# to undersatand this we will use an example-
# we will take a customer feedback -> analyze it (positeive or negative) ->
# on the basis of positive we can then send a form to fill and if it is negative we will send
#  an email stating that out customer executive will connect with you sortly

# architecture ->
# take the feedback -> send it to a model to analyze it, if it is positive or negative
# -> if positive then ask the model to generate a positive response and if negative then send a feedback accourdengly

# the major difference between parallel chain and conditional chain is that -> 
# in ||el chain both chains get executed but in conditional cahin only one will be executed

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda #using RunnableBranch we can execute chain based on condition # Runnablelambda -> it converts a lambda function into Runnable and one it is been converted as Runnable we can use it as chain
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()


llm = HuggingFaceEndpoint(
    # repo_id="google/gemma-2-2b-it",
    repo_id="meta-llama/Llama-3.1-8B-Instruct", # I have used this model becasue it's stronger then google/genmma
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    # max_new_tokens=256,
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

# hear we need to create formate out output because hear we just want the sentiment to be +ve or -ve.
# I have tried without output formating and the output not just a single text it give lots of extra text also.

class Feedback(BaseModel):
    sentiment : Literal['Positive','Negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template= "classif the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2

# this code was to see how the output after parser would look like, but this task will be done by chain (classifier_chain)
# result = classifier_chain.invoke({'feedback': "This is a wonderful smartphone"}) # -> this will give output as -> sentiment='Positive'
# result = classifier_chain.invoke({'feedback': "This is a wonderful smartphone"}).sentiment # -> this will give output as -> Positive
# print(result)

prompt2 = PromptTemplate(
    template = 'Write an appropriate response to this positive feedback \n {feedback}',
    output_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write an appropriate response to this negative feedback \n {feedback}',
    output_variables = ['feedback']
)

branch_chain = RunnableBranch(
    #(condition1, chain1),
    (lambda x:x.sentiment == 'Positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'Negative', prompt3 | model | parser),
    #defualt chain
    RunnableLambda(lambda x: "Could not find sentiment") # hear we need a chain but for defualt we don't have any chain so we used a lambda function and with the help of RunnableLambda we convert that function into runnable and once it is runnable we can use that as a chain.
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))



