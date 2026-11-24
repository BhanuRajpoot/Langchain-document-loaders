from langchain_community.document_loaders import CSVLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

csv_file = "data/sample.csv"
loader = CSVLoader(file_path=csv_file, encoding="utf-8")

documents = loader.load()

print(documents[0].page_content)
