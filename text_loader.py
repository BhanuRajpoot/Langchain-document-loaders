from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = PromptTemplate(
    template="What is the content of the document?",
    input_variables=["document"]
)

perser = StrOutputParser()
chain = prompt | model | perser
loader = TextLoader("data/data.txt", encoding="utf-8")

documents = loader.load()

print(chain.invoke({"document": documents[0]}))
