import pandas as pd

from data.fetch import generate_assets_df
from strategies.rotation import generate_rotation_strategy
from metrics.performance import evaluate_performance

# Defining tickers
tickers = ["SPY", "IEF", "GLD"]

# Uses list of tickers to create a df of close prices
assets = generate_assets_df(tickers)

# Find strategy returns
strategy_returns = generate_rotation_strategy(assets)

# Find Buy & Hold SPY and equal weighted portfolio returns for comparison
buy_and_hold_returns = assets["SPY"].pct_change().dropna()
equal_weighted_returns = assets.pct_change().dropna().mean(axis = 1)

# Evaluate performance by finding cumulative return
print("\nRotation Strategy:\n", evaluate_performance(strategy_returns))
print("\nBuy & Hold:\n", evaluate_performance(buy_and_hold_returns))
print("\nEqual Weighted:\n", evaluate_performance(equal_weighted_returns))


