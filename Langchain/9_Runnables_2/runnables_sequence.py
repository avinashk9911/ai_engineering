from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

#prompt 1
prompt1 = PromptTemplate(
    template= 'Write me a jock about {topic}',
    input_variables= ['topic']
)

#prompt 2
prompt2 = PromptTemplate(
    template= 'Explain the following jock- {text}',
    input_variables= ['text']
)


#model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    # max_new_tokens=256,
)

model = ChatHuggingFace(llm = llm)

#parser
parser = StrOutputParser()

#-------we have created 3 runnables - prompt,model,parser

# now we will create a chain using RunnableSequesce add pass all the runnables 
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
print(chain.invoke({'topic':'AI'}))