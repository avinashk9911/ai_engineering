# we will design a simple chain
# take prompt form the user -> send that to a LLM model -> display the response form llm

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#prompt
prompt = PromptTemplate(
    template = "Generate 5 interesting faces about {topic}",
    input_variables=['topic']
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

# forming chain using our prompt, model and parser
chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'}) # we will invoke out chain and only pass input that is requred in our 1st step i.e input for our prompt i.e. topic

print(result)

# if we want to visualize our chain - first do -> pip install grandalf
chain.get_graph().print_ascii()