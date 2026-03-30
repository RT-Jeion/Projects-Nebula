import pandas as pd

data = pd.read_csv("apple_stocks.csv")

data["MA50d"] = data["Close"].rolling(50).mean()

data["Signal"] = 0

data.loc[50:, "Signal"] = (data.loc[50:, "Close"] > data.loc[50:, "MA50d"]).astype(int)

data["Return"] = data["Close"].pct_change()
data["Strategy"] = data["Return"] * data["Signal"].shift(1)
cumulative_returns = (1 +  data["Strategy"]).cumprod()

print("Cumulative Returns:", cumulative_returns)

data.to_csv("apple_stocks.csv")

cumulative_returns.to_csv("cumulative_reuturns.csv")