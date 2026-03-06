import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq  import ChatGroq

def get_llm():
    return ChatGroq(
        temperature=0.7,
        model="llama-3.1-8b-instant"
    )