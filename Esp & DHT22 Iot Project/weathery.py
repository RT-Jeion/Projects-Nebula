import time
import json
import requests
import pandas as pd
from datetime import datetime
import pytz

# =====================================================
# 🔴 CHANGE THESE
# =====================================================
BOT_TOKEN = "7818206728:AAEGJbjcFEgNEjIA8uxJnfrj_2fDmVwXKaI"
FORECAST_CSV_FILE = "forecast_next_24hours.csv"
TEST_MODE = True   # True = send every minute
# =====================================================

TIMEZONE = "Asia/Dhaka"
tz = pytz.timezone(TIMEZONE)
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"
USERS_FILE = "users.json"


# =====================================================
# USER MANAGEMENT
# =====================================================

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)["users"]
    except:
        return []


def save_user(user_id):
    users = load_users()
    if user_id not in users:
        users.append(user_id)
        with open(USERS_FILE, "w") as f:
            json.dump({"users": users}, f, indent=2)
        print(f"✅ New user added: {user_id}")


# =====================================================
# TELEGRAM
# =====================================================

def send_message(user_id, text):
    res = requests.post(
        f"{TELEGRAM_API}/sendMessage",
        data={"chat_id": user_id, "text": text}
    )
    print(f"📨 Sent to {user_id} | Status: {res.status_code}")


def get_updates(offset):
    return requests.get(
        f"{TELEGRAM_API}/getUpdates",
        params={"offset": offset}
    ).json()


# =====================================================
# FORECAST (FIXED TIME LOGIC)
# =====================================================

def get_current_hour_forecast():
    df = pd.read_csv(FORECAST_CSV_FILE)

    # Convert CSV time (naive) → Dhaka time
    df["time"] = pd.to_datetime(df["time"])
    df["hour_str"] = df["time"].dt.strftime("%Y-%m-%d %H")

    now = datetime.now(tz).strftime("%Y-%m-%d %H")

    print("⏱ Looking for hour:", now)

    row = df[df["hour_str"] == now]

    if row.empty:
        print("❌ No forecast found for this hour")
        return None

    r = row.iloc[0]
    print("✅ Forecast found")

    return (
        f"⏰ Hourly Environment Forecast\n"
        f"🕒 Time: {r['time']}\n\n"
        f"🌡 Temperature: {r['predicted_temp']} °C\n"
        f"💧 Humidity: {r['predicted_rhum']} %\n"
        f"🦠 Mold Risk: {r['mold_risk']}\n"
        f"🧴 Skin Dryness: {r['skin_dryness']}"
    )


# =====================================================
# MAIN LOOP
# =====================================================

def main():
    offset = 0
    print("🤖 Bot running... Send /start")

    while True:
        # Register users
        updates = get_updates(offset)
        for update in updates.get("result", []):
            offset = update["update_id"] + 1
            if "message" in update:
                user_id = update["message"]["chat"]["id"]
                save_user(user_id)
                send_message(user_id, "✅ Subscribed! You will receive alerts.")

        # Send test alerts every minute
        forecast_msg = get_current_hour_forecast()
        if forecast_msg:
            for user in load_users():
                send_message(user, forecast_msg)

        time.sleep(60)


if __name__ == "__main__":
    main()
