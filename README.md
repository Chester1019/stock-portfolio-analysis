# Stock Portfolio Analysis

A beginner-friendly Python project that pulls historical prices for a small set of stocks and calculates the core risk and return measures used in portfolio analysis.

## What this project does

- Downloads daily adjusted closing prices for a chosen set of stocks
- Calculates daily and annualised returns
- Calculates annualised volatility (standard deviation of returns)
- Builds a correlation matrix to show how the stocks move together
- Compares an equal-weighted portfolio against the individual stocks
- Saves a chart and a summary table to the `output/` folder

## Why these measures matter

| Measure | What it tells you |
|---|---|
| Annualised return | The average yearly growth rate of an investment |
| Volatility | How much the price swings; a common proxy for risk |
| Correlation | How similarly two stocks move; low correlation improves diversification |
| Return per unit of risk | A simple ratio of return to volatility, similar to a Sharpe ratio with a 0% risk-free rate |

## How to run it

1. Install Python 3.9 or newer.
2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Open `analysis.py` and edit the `TICKERS` list and date range at the top if you want different stocks.
4. Run:

   ```
   python analysis.py
   ```

Results appear in the `output/` folder.

## Choosing tickers

Tickers follow Yahoo Finance format. Examples:

- Bursa Malaysia: `1155.KL` (Maybank), `1295.KL` (Public Bank), `5347.KL` (Tenaga Nasional)
- US stocks: `AAPL`, `MSFT`
- Indices: `^KLSE` (FTSE Bursa Malaysia KLCI)

## Findings

_Add your own interpretation here after running the script. For example: which stock had the highest return, which had the highest risk, and whether combining them reduced overall volatility._

## Limitations

- Past performance does not predict future results.
- Returns are based on historical prices and ignore transaction costs and taxes.
- The risk-free rate is assumed to be 0% for simplicity.
- Equal weighting is a simplification; real portfolios are often optimised.

## Tools used

Python, pandas, NumPy, matplotlib, yfinance

## About

Created as a personal learning project in finance and data analysis.
