#this this not working because of the new version of langchain. I have to check the new version of langchain and update the code accordingly.

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-4.1-mini")
a=llm.invoke("what is the capital of india?")
print(a.content)




