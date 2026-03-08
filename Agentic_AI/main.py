import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request
from tele_bot import ptb_app, telegram_update

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    await telegram_update(data)
    return {"status": "OK"}

@app.on_event("startup")
async def on_startup():
    webhook_url = f"{os.getenv('WEBHOOK_URL')}/webhook"
    await ptb_app.bot.set_webhook(url=webhook_url)
    print(f"Webhook Set to: {webhook_url}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)