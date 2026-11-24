from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = PromptTemplate(
    template="What is the content of the document?",
    input_variables=["document"] )

perser = StrOutputParser()
chain = prompt | model | perser
loader = DirectoryLoader("data", glob="*.pdf", encoding="utf-8", loader_cls=PyPDFLoader)

documents = loader.load()

print(chain.invoke({"document": documents[0].page_content}))
