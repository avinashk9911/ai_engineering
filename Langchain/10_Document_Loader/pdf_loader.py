#need to download PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"c:\Study\ai_engineering\Langchain\10_Document_Loader\Documentation Index.pdf")
docs = loader.load()
print(docs)
print("Length of Docs------\n", len(docs))
print("First -----\n", docs[0])
print('\n')
print('\n')
print('\n')
print("metadata for first -----\n",docs[1].metadata)

print('\n')
print('\n')
print("metadata for first -----\n",docs[0].page_content)
