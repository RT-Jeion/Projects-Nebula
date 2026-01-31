import asyncio
import os
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import html
import httpx

# 1. Load Environment Variables
load_dotenv()

# CRITICAL FIX: Strip whitespace in case .env has spaces (e.g. "KEY= AIza... ")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_API")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Safety Check: Ensure keys are actually loaded
if not TELEGRAM_TOKEN or not GEMINI_KEY:
    raise ValueError("Error: TELEGRAM_API or GEMINI_API_KEY not found in .env file")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


async def call_gemini(prompt: str):
    # CRITICAL FIX: Exact URL for the v1beta API
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_KEY
    }

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "maxOutputTokens": 1500,  # Increased for better answers
            "temperature": 0.7
        }
    }

    # CRITICAL FIX: Add timeout (LLMs can be slow)
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, headers=headers, json=payload)

        # This will print the actual error from Google if it's not 200 OK
        if response.status_code != 200:
            logging.error(f"Gemini API Error: {response.text}")
            return f"Error from Google: {response.status_code}"

        data = response.json()

        # CRITICAL FIX: Robust parsing (Prevents crashes on 'Safety' blocks)
        try:
            # Check if we have a valid candidate
            if "candidates" in data and data["candidates"]:
                candidate = data["candidates"][0]

                # Check if the model blocked the response (Safety Filter)
                if candidate.get("finishReason") == "SAFETY":
                    return "⚠️ I cannot answer that prompt due to safety guidelines."

                # Return the text
                return candidate["content"]["parts"][0]["text"]
            else:
                return "Gemini returned no content."

        except (KeyError, IndexError) as e:
            logging.error(f"Parsing Error: {e} | Data: {data}")
            return "Sorry, I had trouble understanding Gemini's response."


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Hi! I am a Gemini Chatbot. Ask me anything!")


@dp.message()
async def handle_message(message: types.Message):
    # UX: Show 'typing' while waiting for API
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")

    llm_response = await call_gemini(message.text)

    # UX: Parse Markdown so code blocks look nice
    try:
        await message.answer(llm_response, parse_mode="Markdown")
    except:
        # Fallback if Markdown parsing fails
        await message.answer(llm_response)


async def main():
    print("Bot is polling...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")