import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings

warnings.filterwarnings("ignore")

# -----------------------------
# 1. Load the CSV (replace with your file path if needed)
# -----------------------------
df = pd.read_csv("weather_hourly_3months.csv", parse_dates=['time'], index_col='time')

# Ensure sorted by time
df = df.sort_index()

# -----------------------------
# 2. Preprocess: Handle missing values (linear interpolation)
# -----------------------------
df[['temp', 'rhum']] = df[['temp', 'rhum']].interpolate(method='linear')

# Drop any remaining NaN (e.g., at start)
df = df.dropna()

print(f"Data loaded: {len(df)} rows from {df.index[0]} to {df.index[-1]}")


# -----------------------------
# 3. Feature Engineering
# -----------------------------
def create_features(data):
    df_feat = data.copy()

    # Datetime features
    df_feat['hour'] = df_feat.index.hour
    df_feat['day_of_week'] = df_feat.index.dayofweek

    # Lag features (past values)
    for lag in [1, 2, 3, 24]:
        df_feat[f'temp_lag_{lag}'] = df_feat['temp'].shift(lag)
        df_feat[f'rhum_lag_{lag}'] = df_feat['rhum'].shift(lag)

    # Rolling statistics (past 3 and 6 hours)
    for window in [3, 6]:
        df_feat[f'temp_roll_mean_{window}'] = df_feat['temp'].shift(1).rolling(window=window).mean()
        df_feat[f'temp_roll_std_{window}'] = df_feat['temp'].shift(1).rolling(window=window).std()
        df_feat[f'rhum_roll_mean_{window}'] = df_feat['rhum'].shift(1).rolling(window=window).mean()
        df_feat[f'rhum_roll_std_{window}'] = df_feat['rhum'].shift(1).rolling(window=window).std()

    # Drop rows with NaN from shifting/rolling
    df_feat = df_feat.dropna()
    return df_feat


df_feat = create_features(df)

# Features to use (exclude targets)
feature_cols = [col for col in df_feat.columns if col not in ['temp', 'rhum']]

# -----------------------------
# 4. Time-based Train/Test Split (80% train, 20% test - last part for test)
# -----------------------------
split_idx = int(len(df_feat) * 0.8)
train = df_feat.iloc[:split_idx]
test = df_feat.iloc[split_idx:]

print(f"Train rows: {len(train)}, Test rows: {len(test)}")

# -----------------------------
# 5. Train separate Random Forest models for key horizons
# -----------------------------
horizons = [1, 3, 6, 12, 24]  # hours ahead
models_temp = {}
models_rhum = {}

for h in horizons:
    print(f"\nTraining models for t+{h} hour...")

    # Targets shifted back by h (future values)
    y_temp_train = train['temp'].shift(-h)
    y_rhum_train = train['rhum'].shift(-h)

    # Drop NaN from shift
    X_train = train[feature_cols].iloc[:-h]
    y_temp_train = y_temp_train.iloc[:-h]
    y_rhum_train = y_rhum_train.iloc[:-h]

    # Random Forest
    rf_temp = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42, n_jobs=-1)
    rf_rhum = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42, n_jobs=-1)

    rf_temp.fit(X_train, y_temp_train)
    rf_rhum.fit(X_train, y_rhum_train)

    models_temp[h] = rf_temp
    models_rhum[h] = rf_rhum

# -----------------------------
# 6. Evaluation on Test Set
# -----------------------------
print("\nEvaluation on Test Set:")
for h in horizons:
    X_test = test[feature_cols].iloc[:-h]
    y_temp_true = test['temp'].shift(-h).iloc[:-h]
    y_rhum_true = test['rhum'].shift(-h).iloc[:-h]

    pred_temp = models_temp[h].predict(X_test)
    pred_rhum = models_rhum[h].predict(X_test)

    mae_temp = mean_absolute_error(y_temp_true, pred_temp)
    rmse_temp = np.sqrt(mean_squared_error(y_temp_true, pred_temp))
    mae_rhum = mean_absolute_error(y_rhum_true, pred_rhum)
    rmse_rhum = np.sqrt(mean_squared_error(y_rhum_true, pred_rhum))

    print(
        f"t+{h}h  | Temp MAE: {mae_temp:.2f}°C, RMSE: {rmse_temp:.2f}°C  | RH MAE: {mae_rhum:.2f}%, RMSE: {rmse_rhum:.2f}%")

# -----------------------------
# 7. Predict Next 24 Hours (from the latest data point)
# -----------------------------
latest_data = df_feat.iloc[-1:].copy()  # Last known row

predictions = []
current_features = latest_data[feature_cols].copy()
current_time = latest_data.index[0]

for step in range(1, 25):
    # Determine which model to use (nearest trained horizon)
    horizon = min(horizons, key=lambda x: abs(x - step)) if step not in horizons else step

    # Predict temp and rhum
    pred_temp = models_temp[horizon].predict(current_features)[0]
    pred_rhum = models_rhum[horizon].predict(current_features)[0]

    predictions.append({
        'time': current_time + pd.Timedelta(hours=1),
        'predicted_temp': round(pred_temp, 2),
        'predicted_rhum': round(pred_rhum, 2)
    })

    # Update features recursively for next step (simulate new lags/rolling)
    # Simple update: shift lags and add new values
    new_row = latest_data.copy()
    next_time = current_time + pd.Timedelta(hours=1)
    new_row['temp'] = pred_temp
    new_row['rhum'] = pred_rhum

    # Update lags
    for lag in [1, 2, 3, 24]:
        if lag == 1:
            new_row[f'temp_lag_{lag}'] = pred_temp
            new_row[f'rhum_lag_{lag}'] = pred_rhum
        elif lag in [2, 3]:
            new_row[f'temp_lag_{lag}'] = latest_data[f'temp_lag_{lag - 1}'].values[0]
            new_row[f'rhum_lag_{lag}'] = latest_data[f'rhum_lag_{lag - 1}'].values[0]
        else:  # lag == 24
            prev_24_time = next_time - pd.Timedelta(hours=24)
            if prev_24_time in df.index:
                new_row[f'temp_lag_{lag}'] = df.loc[prev_24_time, 'temp']
                new_row[f'rhum_lag_{lag}'] = df.loc[prev_24_time, 'rhum']
            else:
                # Fallback: keep previous lag_24 if historical lookup isn't available
                new_row[f'temp_lag_{lag}'] = latest_data.get(f'temp_lag_{lag}', pd.Series([np.nan])).values[0]
                new_row[f'rhum_lag_{lag}'] = latest_data.get(f'rhum_lag_{lag}', pd.Series([np.nan])).values[0]

    # Rolling stats (approximate by updating with new value)
    # For simplicity, recalculate rolling on recent predictions (here approximate)
    # In production, maintain a buffer of last 24 values

    # Advance time and state
    new_row.index = pd.DatetimeIndex([next_time])
    latest_data = new_row  # Move forward
    current_features = new_row[feature_cols]
    current_time = next_time

# Create prediction DataFrame
pred_df = pd.DataFrame(predictions)
pred_df = pred_df.set_index('time')

# Add risk assessment columns
def mold_risk_level(temp_c, rh_pct):
    if rh_pct >= 80:
        return "High"
    if 70 <= rh_pct < 80 and 15 <= temp_c <= 30:
        return "Medium"
    return "Low"

def skin_dryness_level(temp_c, rh_pct):
    if rh_pct <= 30 and temp_c >= 20:
        return "High"
    if rh_pct <= 35 or (temp_c >= 28 and rh_pct < 40):
        return "Medium"
    return "Low"

pred_df['mold_risk'] = pred_df.apply(lambda row: mold_risk_level(row['predicted_temp'], row['predicted_rhum']), axis=1)
pred_df['skin_dryness'] = pred_df.apply(lambda row: skin_dryness_level(row['predicted_temp'], row['predicted_rhum']), axis=1)

print("\n=== Next 24-Hour Forecast ===")
print(pred_df)

# Optional: Save predictions
pred_df.to_csv("forecast_next_24hours.csv")
print("\nForecast saved to 'forecast_next_24hours.csv'")