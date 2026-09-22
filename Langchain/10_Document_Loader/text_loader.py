
# if it is giving error - ModuleNotFoundError then do - pip install langchain-community
from langchain_community.document_loaders import TextLoader

# loader = TextLoader('cricket.txt', encoding = 'utf-8')
loader = TextLoader(r"c:\Study\ai_engineering\Langchain\10_Document_Loader\cricket.txt", encoding="utf-8")

docs = loader.load()

print(docs)
print(type(docs)) # it will show that docs is a list
print(len(docs))
print(docs[0]) # out will contain 1) page_content 2) metadata
print(docs[0].page_content)
print(docs[0].metadata)

print(type(docs[0])) #output - <class 'langchain_core.documents.base.Document'>