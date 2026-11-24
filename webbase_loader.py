from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

url = "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview"
loader = WebBaseLoader(url)

print(loader.load()[0].page_content)
