from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

response = model.invoke("Who is the prime minister of India?")

print(response.content)