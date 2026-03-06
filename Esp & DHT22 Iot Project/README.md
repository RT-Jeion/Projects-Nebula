# ESP & DHT22 IoT Project

IoT and weather-analysis workflow that collects sensor/weather data, builds 24-hour forecasts, and reports environment risk indicators.

## What Is Included

- `data_collector.py`: Flask API to receive sensor data and append to `sensor_data.csv`.
- `manual_data_collector.py`: pulls historical hourly temperature/humidity from Open-Meteo.
- `ml_processing.py`: trains RandomForest models and generates next-24-hour forecast.
- `main.py`: prints hourly forecast + risk summary and plots temperature/humidity charts.
- `weathery.py`: Telegram alert script that sends current-hour forecast to subscribed users.

## Data Files

- `weather_hourly_3months.csv`: historical hourly weather data.
- `forecast_next_24hours.csv`: generated 24-hour forecast output.
- `sensor_data.csv`: collected sensor values from API endpoint.

## Workflow

1. Collect history from Open-Meteo using `manual_data_collector.py`.
2. Train and generate forecast using `ml_processing.py`.
3. Run `main.py` to print summary and visualize forecast.
4. Optionally run `data_collector.py` to receive real sensor posts.
5. Optionally run `weathery.py` to push forecast updates via Telegram.

## Install

```bash
pip install pandas numpy matplotlib scikit-learn flask requests pytz
```

## Run Examples

### A) Build/refresh historical weather dataset

```bash
python manual_data_collector.py
```

### B) Train model and generate 24-hour forecast

```bash
python ml_processing.py
```

### C) Show summary and forecast plots

```bash
python main.py
```

### D) Start sensor ingestion API

```bash
python data_collector.py
```

API endpoint:

- `POST /data`
- JSON fields required: `timestamp`, `temperature`, `humidity`

### E) Send Telegram forecast messages

```bash
python weathery.py
```

## Notes

- `main.py` auto-runs `ml_processing.py` if forecast data is missing/stale.
- Forecast risk labels use heuristic thresholds for:
  - mold risk
  - skin dryness risk
- `weathery.py` currently contains a hardcoded bot token; move this to environment variables before sharing/deployment.
