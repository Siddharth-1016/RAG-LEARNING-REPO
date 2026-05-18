from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
import os

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)