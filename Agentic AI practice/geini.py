import asyncio

from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

user_prompt = input("Enter your prompt:\n")

async def main():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = await client.aio.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{user_prompt}. Answer in 3 line line"

    )
    print("\nGemini's Response:")
    print(response.text)

asyncio.run(main())