import requests
import pandas as pd
from datetime import datetime, timedelta

# Your location (near Dhaka, Bangladesh)
lat = 23.833489394276658
lon = 90.55435506600828

# Time range: last ~3 months (90 days) up to now
# NOTE: The start/end dates must still be calculated based on the current UTC time
# for the API to correctly determine the 90-day period.
end = datetime.utcnow()
start = end - timedelta(days=90)

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": lat,
    "longitude": lon,
    "start_date": start.strftime("%Y-%m-%d"),
    "end_date": end.strftime("%Y-%m-%d"),
    "hourly": "temperature_2m,relative_humidity_2m",
    # *** CHANGE IS HERE: Request the data in the GMT time zone from the API ***
    "timezone": "GMT"
}

response = requests.get(url, params=params)

if response.status_code != 200:
    print("Error fetching data:", response.text)
else:
    data = response.json()["hourly"]

    df = pd.DataFrame({
        "time": data["time"],
        "temp": data["temperature_2m"],  # Temperature in °C
        "rhum": data["relative_humidity_2m"]  # Relative humidity in %
    })

    df["time"] = pd.to_datetime(df["time"])
    df = df.set_index("time")
    df = df.dropna()

    # NOTE: The timestamps in df.index are now GMT+6:00 (since the API handles the conversion).

    # Save to CSV
    df.to_csv("weather_hourly_3months.csv")

    # Verify
    print("Total rows:", len(df))
    print("\n--- GMT+6 Time Head ---")
    print(df.head())
    print("\n--- GMT+6 Time Tail ---")
    print(df.tail())