from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Random_Forest_Interview_QA.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].metadata)

print(docs[0])