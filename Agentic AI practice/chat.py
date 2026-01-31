import asyncio
import logging
import os
from google import genai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import html
from dotenv import load_dotenv

load_dotenv()

Telegram_token = os.getenv("TELEGRAM_API")

gemini_list = [os.getenv()]

bot = Bot(token=Telegram_token)
dp = Dispatcher()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
chat = client.aio.chats.create(model="gemini-2.5-flash")

async def call_gemini(text: str):
    response = await chat.send_message(text)
    return response.text


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Hi! I am a Gemini Chatbot. Ask me anything!")


@dp.message()
async def handle_message(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    llm_response = await call_gemini(message.text)

    try:
        await message.answer(llm_response, parse_mode="Markdown")
    except:
        await message.answer(llm_response)


async def main():
    print("Bot is polling...")
    await dp.start_polling(bot)
logging.basicConfig(level=logging.INFO)
asyncio.run(main())