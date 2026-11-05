"""
Stock Portfolio Analysis
------------------------
Downloads historical prices, then calculates returns, volatility,
correlations, and an equal-weighted portfolio.

Edit the settings below, then run:  python analysis.py
"""

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

# ----------------------------- Settings -----------------------------
TICKERS = ["1155.KL", "1295.KL", "5347.KL", "AAPL"]  # edit these
START_DATE = "2021-01-01"
END_DATE = "2025-12-31"
TRADING_DAYS = 252  # approximate trading days in a year
OUTPUT_DIR = "output"
# --------------------------------------------------------------------


def download_prices(tickers, start, end):
    """Download adjusted closing prices for the given tickers."""
    data = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)
    prices = data["Close"]
    if isinstance(prices, pd.Series):
        prices = prices.to_frame(name=tickers[0])
    return prices.dropna(how="all").ffill().dropna()


def summarise(returns):
    """Build a summary table of annualised return, volatility and return/risk."""
    annual_return = returns.mean() * TRADING_DAYS
    annual_vol = returns.std() * np.sqrt(TRADING_DAYS)
    summary = pd.DataFrame(
        {
            "Annualised return": annual_return,
            "Annualised volatility": annual_vol,
            "Return per unit of risk": annual_return / annual_vol,
        }
    )
    return summary


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prices = download_prices(TICKERS, START_DATE, END_DATE)
    print(f"Downloaded {len(prices)} trading days for {list(prices.columns)}\n")

    # Daily returns
    returns = prices.pct_change().dropna()

    # Equal-weighted portfolio
    weights = np.repeat(1 / len(prices.columns), len(prices.columns))
    returns["PORTFOLIO"] = returns[prices.columns].dot(weights)

    # Summary table
    summary = summarise(returns)
    print("Summary (annualised):")
    print(summary.round(3), "\n")
    summary.round(4).to_csv(os.path.join(OUTPUT_DIR, "summary.csv"))

    # Correlation matrix
    corr = returns[prices.columns].corr()
    print("Correlation matrix:")
    print(corr.round(2), "\n")
    corr.round(4).to_csv(os.path.join(OUTPUT_DIR, "correlation.csv"))

    # Chart: growth of 1 unit invested
    growth = (1 + returns).cumprod()
    ax = growth.plot(figsize=(10, 6))
    ax.set_title("Growth of 1 unit invested")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "growth_chart.png"), dpi=150)
    plt.close()

    print(f"Saved results to the '{OUTPUT_DIR}' folder.")


if __name__ == "__main__":
    main()
