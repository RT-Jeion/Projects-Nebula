# Quant Trading Practice

A small practice project for downloading Apple (AAPL) historical data and testing a simple moving-average strategy.

## What This Project Does

- Downloads AAPL price history from Yahoo Finance.
- Calculates a 50-day moving average (`MA50d`).
- Generates a long-only signal:
  - `1` when `Close > MA50d`
  - `0` otherwise
- Computes daily strategy returns and cumulative returns.
- Saves updated datasets to CSV files.

## Files

- `get_data.py`: Downloads historical AAPL data and writes `apple_stocks.csv`.
- `analyse_data.py`: Builds indicators/signals and writes strategy output.
- `apple_stocks.csv`: Source and processed market data.
- `cumulative_reuturns.csv`: Saved cumulative return series.
- `requirments.txt`: Dependency list file (current filename uses this spelling).

## Requirements

Python 3.9+ recommended.

Main libraries used by the scripts:

- pandas
- yfinance

Install dependencies:

```bash
pip install -r requirments.txt
```

If `requirments.txt` has encoding issues in your environment, install manually:

```bash
pip install pandas yfinance
```

## How To Run

From this folder:

```bash
python get_data.py
python analyse_data.py
```

## Output

After running:

- `apple_stocks.csv` contains downloaded data plus computed columns (`MA50d`, `Signal`, `Return`, `Strategy`).
- `cumulative_reuturns.csv` contains the cumulative strategy return series.

## Notes

- The script currently overwrites `apple_stocks.csv` with calculated columns.
- The filenames `requirments.txt` and `cumulative_reuturns.csv` are kept as-is to match existing project files.
