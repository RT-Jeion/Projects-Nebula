import os
from dotenv import load_dotenv
load_dotenv()
from telegram import Update
from telegram.ext import Application
from telegram.constants import ChatAction
from agent import agent_executor

token = os.getenv("TELEGRAM_API_KEY")
ptb_app = Application.builder().token(token).build()

async def telegram_update(update_data: dict):
    """Processes the raw JSON from FastAPI and runs the agent"""
    update = Update.de_json(update_data, ptb_app.bot)

    if not update.message or not update.message.text:
        return

    user_id = str(update.message.chat_id)
    user_text = update.message.text

    await ptb_app.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)

    response = await agent_executor.ainvoke(
        {"input": user_text},
        config={"configurable": {"session_id": user_id}}
    )

    response_text = getattr(response, "content", str(response))
    await update.message.reply_text(response_text)