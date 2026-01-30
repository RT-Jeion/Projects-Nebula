import os
import sys
import subprocess
from datetime import timedelta

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


HIST_CSV = "weather_hourly_3months.csv"
FORECAST_CSV = "forecast_next_24hours.csv"
ML_SCRIPT = "ml_processing.py"


def load_history(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["time"], index_col="time")
    df = df.sort_index()
    # Basic cleaning (keep consistent with ml_processing)
    if {"temp", "rhum"}.issubset(df.columns):
        df[["temp", "rhum"]] = df[["temp", "rhum"]].interpolate(method="linear")
        df = df.dropna()
    return df


def ensure_forecast_up_to_date(history: pd.DataFrame) -> pd.DataFrame:
    latest_time = history.index[-1]
    need_run = True
    if os.path.exists(FORECAST_CSV):
        try:
            fc = pd.read_csv(FORECAST_CSV, parse_dates=["time"], index_col="time")
            fc = fc.sort_index()
            # Expect first forecast time to be latest + 1h
            if not fc.empty and fc.index[0] == latest_time + pd.Timedelta(hours=1):
                need_run = False
                return fc
        except Exception:
            need_run = True

    if need_run:
        # Run ml_processing.py to regenerate forecast
        py = sys.executable or "python"
        completed = subprocess.run([py, ML_SCRIPT], cwd=os.getcwd())
        if completed.returncode != 0:
            raise RuntimeError("Failed to generate forecast via ml_processing.py")
        fc = pd.read_csv(FORECAST_CSV, parse_dates=["time"], index_col="time").sort_index()
        return fc


def mold_risk_level(temp_c: float, rh_pct: float) -> str:
    # Simple heuristic: high risk when RH very high; moderate at high RH with suitable temps
    if rh_pct >= 80:
        return "High"
    if 70 <= rh_pct < 80 and 15 <= temp_c <= 30:
        return "Medium"
    return "Low"


def skin_dryness_level(temp_c: float, rh_pct: float) -> str:
    # Simple heuristic: low RH → dryness; elevated temps with low RH worsen it
    if rh_pct <= 30 and temp_c >= 20:
        return "High"
    if rh_pct <= 35 or (temp_c >= 28 and rh_pct < 40):
        return "Medium"
    return "Low"


def aggregate_levels(levels: list[str]) -> str:
    # Map levels to scores and back
    score_map = {"Low": 0, "Medium": 1, "High": 2}
    inv_map = {v: k for k, v in score_map.items()}
    scores = [score_map.get(x, 0) for x in levels]
    avg = np.mean(scores) if scores else 0
    # Round to nearest level
    return inv_map[int(round(avg))]


def _last_7_days(history: pd.DataFrame) -> pd.DataFrame:
    last_7d_start = history.index[-1] - pd.Timedelta(days=7)
    return history.loc[last_7d_start:]


def plot_temperature(history: pd.DataFrame, forecast: pd.DataFrame, save_path: str | None = None) -> None:
    hist_7d = _last_7_days(history)
    current_time = history.index[-1]

    plt.figure(figsize=(12, 4.5))
    plt.plot(hist_7d.index, hist_7d["temp"], color="tab:red", label="Temp (hist)")
    plt.axvline(current_time, color="gray", linestyle=":", linewidth=1)
    plt.scatter([current_time], [hist_7d.loc[current_time, "temp"]], color="tab:red", zorder=5)
    plt.plot(forecast.index, forecast["predicted_temp"], color="tab:red", linestyle="--", label="Temp (forecast)")
    plt.axvspan(forecast.index[0], forecast.index[-1], color="gray", alpha=0.1, label="Forecast window")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature: Last 7 Days + Next 24 Hours")
    plt.xlabel("Time")
    plt.legend(loc="upper left")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_humidity(history: pd.DataFrame, forecast: pd.DataFrame, save_path: str | None = None) -> None:
    hist_7d = _last_7_days(history)
    current_time = history.index[-1]

    plt.figure(figsize=(12, 4.5))
    plt.plot(hist_7d.index, hist_7d["rhum"], color="tab:blue", label="RH (hist)")
    plt.axvline(current_time, color="gray", linestyle=":", linewidth=1)
    # For marker, guard if RH missing at current_time in window (unlikely after cleaning)
    if current_time in hist_7d.index:
        plt.scatter([current_time], [hist_7d.loc[current_time, "rhum"]], color="tab:blue", zorder=5)
    plt.plot(forecast.index, forecast["predicted_rhum"], color="tab:blue", linestyle="--", label="RH (forecast)")
    plt.axvspan(forecast.index[0], forecast.index[-1], color="gray", alpha=0.1, label="Forecast window")
    plt.ylabel("Relative Humidity (%)")
    plt.title("Humidity: Last 7 Days + Next 24 Hours")
    plt.xlabel("Time")
    plt.legend(loc="upper left")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def print_terminal_summary(latest_time: pd.Timestamp, forecast: pd.DataFrame) -> None:
    print(f"Latest Data Timestamp: {latest_time}")
    print("Next 24 Hours Forecast:")

    mold_levels = []
    dryness_levels = []

    # Ensure correct order
    fc = forecast.sort_index()
    for i, (ts, row) in enumerate(fc.iterrows(), start=1):
        t = float(row["predicted_temp"])  # °C
        h = float(row["predicted_rhum"])  # %
        mold = mold_risk_level(t, h)
        dry = skin_dryness_level(t, h)
        mold_levels.append(mold)
        dryness_levels.append(dry)
        print(
            f"Hour {i:>2} | Temp: {t:.1f}°C | RH: {h:.0f}% | Mold Risk: {mold} | Skin Dryness: {dry}"
        )

    overall_mold = aggregate_levels(mold_levels)
    overall_dry = aggregate_levels(dryness_levels)
    print(f"\nOverall 24-Hour Summary: Mold Risk: {overall_mold} | Skin Dryness: {overall_dry}")


def main():
    if not os.path.exists(HIST_CSV):
        raise FileNotFoundError(f"Missing historical CSV: {HIST_CSV}")

    history = load_history(HIST_CSV)
    forecast = ensure_forecast_up_to_date(history)

    latest_time = history.index[-1]
    print_terminal_summary(latest_time, forecast)

    # Plot and save images
    plot_temperature(history, forecast, save_path="temperature_forecast_plot.png")
    plot_humidity(history, forecast, save_path="humidity_forecast_plot.png")


if __name__ == "__main__":
    main()
