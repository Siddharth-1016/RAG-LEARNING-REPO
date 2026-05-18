from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
import os

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary for the following poem \n {poem}',
    input_variables=['poem']
)

chain = prompt | model | parser
print(chain.invoke({'poem':docs[0].page_content}))
