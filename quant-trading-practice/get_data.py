import yfinance as yf
import pandas as pd

symbol = "AAPL"

data = yf.download(symbol, start="2023-01-01")

data.to_csv("apple_stocks.csv")