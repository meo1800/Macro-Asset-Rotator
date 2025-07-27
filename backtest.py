import pandas as pd

from data.fetch import get_asset_data
from strategies.rotation import generate_rotation_strategy
from metrics.performance import evaluate_performance

# Defining tickers
tickers = ["SPY", "IEF", "GLD"]


# Creates dictionary of single column df's for each ticker
data = {}

for symbol in tickers:
    print(f"Getting data for {symbol}")
    asset_df = get_asset_data(symbol)
    data[symbol] = asset_df

# Concatenates the data for each ticker into one data frame
assets = pd.concat(data.values(), axis = 1)
assets.dropna(inplace = True)

# Find strategy returns
print("Generating strategy...")
strategy_returns = generate_rotation_strategy(assets)

# Find Buy & Hold SPY and equal weighted portfolio returns for comparison
buy_and_hold_returns = assets["SPY"].pct_change().dropna()
equal_weighted_returns = assets.pct_change().dropna().mean(axis = 1)

# Evaluate performance by finding cumulative return
print("Rotation Strategy:\n", evaluate_performance(strategy_returns))
print("\nBuy & Hold:\n", evaluate_performance(buy_and_hold_returns))
print("\nEqual Weighted:\n", evaluate_performance(equal_weighted_returns))


