
from dotenv import load_dotenv
# from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     max_new_tokens=100,
# )

# chat_model = ChatHuggingFace(llm=llm)

# response = chat_model.invoke(
#     "What is artificial intelligence? Explain in simple words."
# )

# print(response.content)



from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device=-1,
)

prompt = """<|system|>
You are a helpful assistant.</s>
<|user|>
What is artificial intelligence? Explain in simple words.</s>
<|assistant|>
"""

result = generator(
    prompt,
    max_new_tokens=100,
    do_sample=False,
)

print(result[0]["generated_text"])
