
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

text = "LangChain makes it easier to work with language models."

vector = embeddings.embed_query(text)

print("Text:", text)
print("Vector length:", len(vector))
print("First 10 numbers:", vector[:10])
