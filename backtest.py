import pandas as pd

from data.fetch import generate_assets_df
from strategies.rotation import generate_rotation_strategy
from strategies.multi_signal import generate_multi_signal_strategy
from metrics.performance import evaluate_performance
from visuals.plots import plot_cum_returns
from utils.backtest_extras import bl_evaluation_comparison, total_results_dict

# Defining tickers
tickers = ["SPY", "IEF", "GLD"]

# Uses list of tickers to create a df of close prices
assets = generate_assets_df(tickers)

# Find strategy returns
rotation_strategy_results = generate_rotation_strategy(assets)
multi_signal_strategy = generate_multi_signal_strategy(assets)

# Evaluates performance of the strategy with each delay scenario with comparison to baseline returns and optio
bl_evaluation_comparison(assets, rotation_strategy_results, multi_signal_strategy)

# Creates dict with results of strategies and baselines
results_dict = total_results_dict(assets, rotation_strategy_results, multi_signal_strategy)

# Plot returns using returns dictionary
plot_cum_returns(results_dict)

# print(strategy_results.describe())