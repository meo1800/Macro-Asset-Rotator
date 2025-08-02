import pandas as pd
import numpy as np

def genereate_top_performers_strategy(assets, window = 21, top_n = 2, max_delay = 1):
    
    # Calculates percentage change during window
    momentum = assets.pct_change(periods = window)

    # Ranks different assets depending on their trailing performance in descending order
    ranked = momentum.rank(axis = 1, ascending = False)

    # Signal returns True for assets within the specified top_n
    signal = (ranked <= top_n).astype(float)

    # Normalizes the signal by finding the equal weighted combination of top_n assets
    signal = signal.div(signal.sum(axis = 1), axis = 0) 

    # Reindexes daily returns as NaNs were dropped from signal
    daily_returns = assets.pct_change().dropna()

    results = {}

    # Appyling signal to each delay scenario in the range
    for delay in range (1, max_delay + 1):
        shifted_signal = signal.shift(delay).reindex(daily_returns.index).dropna()
        
        returns = []

        for date, weight in shifted_signal.iterrows():
            returns.append((daily_returns.loc[date] * weight).sum())

        strategy_returns = pd.Series(returns, index = shifted_signal.index)
        results[delay] = strategy_returns

    return results