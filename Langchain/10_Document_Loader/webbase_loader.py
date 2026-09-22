from langchain_community.document_loaders import WebBaseLoader

url = "https://www.flipkart.com/apple-2022-macbook-air-m2-8-gb-256-gb-ssd-mac-os-monterey-mly33hn-a/p/itm0946c05e6335c"
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)