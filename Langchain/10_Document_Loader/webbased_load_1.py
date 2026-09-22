# need to install beautiful soup - pip install beautifulsoup4 lxml
# if it is giving error - ModuleNotFoundError then do - pip install langchain-community
from langchain_community.document_loaders import TextLoader, WebBaseLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

# url = "https://www.flipkart.com/apple-2022-macbook-air-m2-8-gb-256-gb-ssd-mac-os-monterey-mly33hn-a/p/itm0946c05e6335c"
url = "https://www.w3schools.com/cs/cs_methods.php"
loader = WebBaseLoader(url)

docs = loader.load()


llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Llama-3.2-1B-Instruct',
    task = 'conversational',
    provider = 'featherless-ai'
)
model = ChatHuggingFace(llm = llm)

#prompt
prompt = PromptTemplate(
    template = 'Anaswer the following question {question} \n form the following text -\n {text}',
    input_variables=['question','text']
)

#parser
parser = StrOutputParser()


#chain
chain = prompt | model | parser

result = chain.invoke({'question': 'what is the product that we are taking about', 'text': docs[0].page_content})
print(result)