# Agentic AI Telegram Chatbot

A Telegram chatbot served through FastAPI webhook endpoints and powered by a Groq LLM via LangChain.

## What This Project Does

- Exposes a FastAPI server with a webhook endpoint at `/webhook`.
- Receives Telegram updates and passes them to a LangChain chat agent.
- Uses per-user conversation memory (keyed by Telegram `chat_id`).
- Replies back to users in Telegram with model-generated responses.

## Current Stack

- `FastAPI` for the web server.
- `python-telegram-bot` for Telegram update/message handling.
- `LangChain` for prompt + history pipeline.
- `langchain-groq` with model `llama-3.1-8b-instant`.
- `python-dotenv` for environment variables.

## Project Files

- `main.py`: FastAPI app, `/webhook` route, webhook setup on startup.
- `tele_bot.py`: parses Telegram updates, sends typing status, invokes agent, sends reply.
- `agent.py`: creates LangChain runnable with message history.
- `llm_sertup.py`: initializes Groq chat model.

## Environment Variables

Create a `.env` file in `Agentic AI/` with:

```env
TELEGRAM_API_KEY=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
WEBHOOK_URL=https://your-public-domain
```

Notes:
- `WEBHOOK_URL` must be publicly reachable by Telegram.
- The app automatically registers webhook as `${WEBHOOK_URL}/webhook` on startup.

## Install

From `Agentic AI/`:

```bash
pip install fastapi uvicorn python-dotenv python-telegram-bot langchain langchain-community langchain-core langchain-groq
```

## Run

From `Agentic AI/`:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

When the server starts, it sets the Telegram webhook and logs:

```text
Webhook Set to: <WEBHOOK_URL>/webhook
```

## Request Flow

1. Telegram sends message update to `/webhook`.
2. `main.py` calls `telegram_update(...)`.
3. `tele_bot.py` invokes the LangChain agent with `session_id = chat_id`.
4. Agent uses stored history and generates a response.
5. Bot replies to the same Telegram chat.

## Important Behavior

- Conversation memory is in-process (`store = {}` in `agent.py`).
- Restarting the app clears chat history.
- Non-text Telegram updates are ignored.