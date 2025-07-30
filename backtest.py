import pandas as pd

from data.fetch import generate_assets_df
from strategies.rotation import generate_rotation_strategy
from metrics.performance import evaluate_performance
from visuals.plots import plot_cum_returns
from utils.backtest_extras import get_base_line_returns

# Defining tickers
tickers = ["SPY", "IEF", "GLD"]

# Uses list of tickers to create a df of close prices
assets = generate_assets_df(tickers)

# Find strategy returns

strategy_returns = generate_rotation_strategy(assets)

# Find Buy & Hold SPY and equal weighted portfolio returns for comparison
buy_and_hold_returns, equal_weighted_returns = get_base_line_returns(assets)

# Evaluate performance by finding cumulative return

for delay, returns in strategy_returns.items():
    print(f"\n{delay}d Delay Rotation Strategy:\n", evaluate_performance(returns))

print("\nBuy & Hold:\n", evaluate_performance(buy_and_hold_returns))
print("\nEqual Weighted:\n", evaluate_performance(equal_weighted_returns))

# Dictionary of labels and return data
returns_dict = {}

# Loop through each delay scenario of the strategy returns
for delay, returns in strategy_returns.items():
    label = f"{delay}d Delay Rotation Strategy"
    returns_dict[label] = returns

# For comparison     
returns_dict["Buy & Hold"] = buy_and_hold_returns
returns_dict["Equal Weighted"] = equal_weighted_returns

# Plot returns using returns dictionary
plot_cum_returns(returns_dict)

# print(strategy_returns.describe())