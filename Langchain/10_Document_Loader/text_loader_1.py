# now we will add a llm to our text

# if it is giving error - ModuleNotFoundError then do - pip install langchain-community
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

# loader = TextLoader('cricket.txt', encoding = 'utf-8')
loader = TextLoader(r"c:\Study\ai_engineering\Langchain\10_Document_Loader\cricket.txt", encoding="utf-8")
docs = loader.load()
print(docs[0].length)


llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Llama-3.2-1B-Instruct',
    task = 'conversational',
    provider = 'featherless-ai'
)
model = ChatHuggingFace(llm = llm)

#prompt
prompt = PromptTemplate(
    template = 'Write a summary for the following poem {poem}',
    input_variables=['poem']
)

#parser
parser = StrOutputParser()


#chain
chain = prompt | model | parser

result = chain.invoke(docs[0].page_content)
print(result)