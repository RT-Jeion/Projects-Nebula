from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = "sensor_data.csv"

# Create CSV with header if not exists
if not os.path.isfile(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "humidity"])

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    timestamp = data.get("timestamp")
    temperature = data.get("temperature")
    humidity = data.get("humidity")

    if None in (timestamp, temperature, humidity):
        return jsonify({"error": "Missing fields"}), 400

    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, temperature, humidity])

    print("Saved:", timestamp, temperature, humidity)

    return jsonify({"status": "success"}), 200


@app.route("/")
def home():
    return "ESP8266 CSV Logger Running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
