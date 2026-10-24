
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

documents = [
    "I love learning Python.",
    "Python programming is interesting.",
    "Today the weather is rainy.",
]

vectors = embeddings.embed_documents(documents)

print("Number of documents:", len(documents))
print("Number of vectors:", len(vectors))
print("Dimensions of first vector:", len(vectors[0]))

print("\nFirst vector, first 5 numbers:")
print(vectors[0][:5])
