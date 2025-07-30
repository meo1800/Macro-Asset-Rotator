import pandas as pd
import numpy as np

# Combine volatility and momentum signals into a rotation strategy
def generate_multi_signal_strategy(assets, window = 21, volatility_window = 5, max_delay = 1):

    # Calculates percentage change during window
    momentum = assets.pct_change(periods = window)

    # Created rolling volatility window
    volatility = assets.pct_change().rolling(volatility_window).std()

    # Rank across assets columns for each day
    momentum_rank = momentum.rank(axis = 1, ascending = False)
    volatility_rank = volatility.rank(axis = 1, ascending = True)
    combined_score = momentum_rank + volatility_rank

    # Signal returns asset column with lowest score (best rank)
    signal = combined_score.dropna().idxmin(axis = 1)

    daily_returns = assets.pct_change().dropna()
    
    results = {}

    # Appyling signal to each delay scenario in the range
    for delay in range (1, max_delay + 1):
        shifted_signal = signal.shift(delay).reindex(daily_returns.index).dropna()
        returns = []

        for date, asset in shifted_signal.items():
            returns.append(daily_returns.loc[date, asset])
        strategy_returns = pd.Series(returns, index = shifted_signal.index)
        results[delay] = strategy_returns

    return results

