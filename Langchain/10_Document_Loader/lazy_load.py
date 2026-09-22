# We will learn about leazy load

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = r'C:\Study\ai_engineering\Langchain\10_Document_Loader\Books', # we can't just pass path="Books" because Python looks for it from the current working directory (where you ran the command), not from the script’s folder.  You ran from: C:\Study\ai_engineering\Langchain  So path="Books" means:C:\Study\ai_engineering\Langchain\10_Document_Loader\Books ← does not exist
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)