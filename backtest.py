import pandas as pd

from data.fetch import generate_assets_df
from strategies.rotation import generate_rotation_strategy
from metrics.performance import evaluate_performance
from visuals.plots import plot_cum_returns
from utils.backtest_extras import bl_evaluation_comparison

# Defining tickers
tickers = ["SPY", "IEF", "GLD"]

# Uses list of tickers to create a df of close prices
assets = generate_assets_df(tickers)

# Find strategy returns
rotation_strategy_results = generate_rotation_strategy(assets)

# Evaluates performance of the strategy with each delay scenario with comparison to baseline returns and optio
bl_evaluation_comparison(rotation_strategy_results, assets)

# Dictionary of labels and return data
returns_dict = {}

# Loop through each delay scenario of the strategy returns
for delay, returns in strategy_results.items():
    label = f"{delay}d Delay Rotation Strategy"
    returns_dict[label] = returns

# For comparison     
returns_dict["Buy & Hold"] = buy_and_hold_returns
returns_dict["Equal Weighted"] = equal_weighted_returns

# Plot returns using returns dictionary
plot_cum_returns(returns_dict)

# print(strategy_results.describe())