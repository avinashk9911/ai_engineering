from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Study\ai_engineering\Langchain\11_Text_Splitters\Document\NIPS-2017-attention-is-all-you-need-Paper.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_documents(docs)
print(result[0]) # first list of chunks, this will contain meta data and page content
print('\n')
print(result[0].page_content)