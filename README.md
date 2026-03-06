# Projects-Nebula

Personal project repository built during an AI and Python learning journey.

## Repository Overview

This repo contains multiple independent mini-projects and experiments:

- `Agentic AI/`: Telegram chatbot with FastAPI webhook + LangChain + Groq.
- `Esp & DHT22 Iot Project/`: sensor-data collection, weather forecasting, and risk analysis scripts.
- `Leetcode/`: algorithm practice solutions.
- `Coin Flip/`: probability simulation scripts for repeated coin tosses.
- `Python/`: beginner-to-intermediate Python console apps and exercises.
- `AI engineering roadmap.md`: planning notes and learning roadmap.

## Project Details

### 1. Agentic AI

Path: `Agentic AI/`

What it does:
- Runs a FastAPI server with `/webhook` endpoint for Telegram updates.
- Uses `python-telegram-bot` to process messages.
- Uses LangChain message history per user session.
- Uses Groq model `llama-3.1-8b-instant` for responses.

Main files:
- `Agentic AI/main.py`
- `Agentic AI/tele_bot.py`
- `Agentic AI/agent.py`
- `Agentic AI/llm_sertup.py`
- `Agentic AI/README.md`

### 2. ESP & DHT22 IoT Project

Path: `Esp & DHT22 Iot Project/`

What it does:
- `data_collector.py`: Flask API endpoint (`/data`) to receive and append sensor readings into `sensor_data.csv`.
- `manual_data_collector.py`: downloads historical hourly weather data from Open-Meteo and writes `weather_hourly_3months.csv`.
- `ml_processing.py`: trains RandomForest regressors for temperature/humidity forecasting and exports `forecast_next_24hours.csv`.
- `main.py`: loads history + forecast, prints hourly mold/skin-dryness risk summary, and plots last 7 days + next 24 hours.
- `weathery.py`: Telegram broadcast utility for hourly forecast alerts.

Data files currently included:
- `Esp & DHT22 Iot Project/weather_hourly_3months.csv`
- `Esp & DHT22 Iot Project/forecast_next_24hours.csv`
- `Esp & DHT22 Iot Project/sensor_data.csv`

### 3. LeetCode Practice

Path: `Leetcode/1. Two Sum/`

Includes:
- `Two Sum(One pass).py`: hash-map one-pass approach.
- `Two Sum(Two pass).py`: hash-map two-pass style approach.
- `README.md`: explanation and complexity notes.

### 4. Coin Flip Simulations

Path: `Coin Flip/`

Includes:
- `coin flip.py`: simple interactive 5-toss simulation.
- `Coin flip counter.py`: repeated large-trial runs with head/tail percentages and average gap reporting.

### 5. Python Exercises

Path: `Python/`

Subprojects:
- `Calculator/calculator.py`: expression-based calculator with recall history.
- `Greedy Algorithm/`: coin-change style greedy scripts (fixed and user-defined denominations).
- `Number Sync/number sync.py`: prints padded numbered labels (e.g., `001.Name`).
- `Versity Project/bank.py`: CLI bank system with account creation, PIN check, history, deposit, and withdraw.
- `Versity Project/calculator.py`: menu-driven calculator with basic arithmetic, average, and square root.

## Quick Start

Each folder is an independent project. Run scripts from inside that project directory.

Example:

```bash
cd "Agentic AI"
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

For algorithm/practice scripts, run directly:

```bash
python "Leetcode/1. Two Sum/Two Sum(One pass).py"
```

## Notes

- Most projects are learning-focused and may favor readability and experimentation over production structure.
- Some scripts include hardcoded test inputs for quick local runs.
