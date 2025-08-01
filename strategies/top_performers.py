import pandas as pd
import numpy as np

def genereate_top_performers_strategy(assets, window = 21, top_n = 2, delay = 1):
    
    # Calculates percentage change during window
    momentum = assets.pct_change(periods = window)

    # Ranks different assets depending on their trailing performance in descending order
    ranked = momentum.rank(axis = 1, ascending = False)

    # Signal returns True for assets within the specified top_n
    signal = (ranked <= top_n).astype(float)

    # Normalizes the signal by finding the equal weighted combination of top_n assets
    signal = signal.div(signal.sum(axis = 1, axis = 0))

    # Appyling signal delay to simulate execution lag
    signal = signal.shift(delay).reindex(assets.index).dropna()

    # Reindexes daily returns as NaNs were dropped from signal
    daily_returns = assets.pct_change().reindex(signal.index)

    # Returns the signal weighted return across asset columns
    strategy_returns = (daily_returns * signal).sum(axis = 1)

    return strategy_returns