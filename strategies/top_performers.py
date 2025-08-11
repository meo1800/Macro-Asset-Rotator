import pandas as pd
import numpy as np


def genereate_top_performers_strategy(assets, window = 21, top_n = 2, max_delay = 1, weighting = "momentum"):
    
    # Calculates percentage change during window
    momentum = assets.pct_change(periods = window)

    # Ranks different assets depending on their trailing performance in descending order
    ranked = momentum.rank(axis = 1, ascending = False)

    if weighting == "equal":
        # Signal returns True for assets within the specified top_n
        signal = (ranked <= top_n).astype(float)

        # Normalizes the signal by finding the equal weighted combination of top_n assets
        signal = signal.div(signal.sum(axis = 1), axis = 0) 
    
    # Provides an optional momentum weighted portfolio
    elif weighting == "momentum":
        top_performers = (ranked <= top_n)
        # Keep only positive momentum values for weighting
        top_n_momentum = momentum.where(top_performers & (momentum > 0), 0.0)
        # Sum only positive momentum to normalize weights and ignore days with no positive momentum
        row_sums = top_n_momentum.sum(axis=1).where(lambda x: x > 0, np.nan)
        signal = top_n_momentum.div(row_sums, axis=0).fillna(0)
        
        # # Ensure no all mean sum is approx 1 with minimal std
        # print("Signal row sum stats:")
        # print(signal.sum(axis=1).describe())
        # print(signal.loc[signal.index[-1]])

    # Reindexes daily returns as NaNs were dropped from signal
    daily_returns = assets.pct_change().dropna()

    results = {}

    # # Prints No. of rows containing Nans
    # print("Signal NaN rows:", signal.isna().any(axis=1).sum())

    # Appyling signal to each delay scenario in the range
    for delay in range (1, max_delay + 1):
        shifted_signal = signal.shift(delay).reindex(daily_returns.index).dropna()
        
        returns = []
        valid_dates = []
            
        for date, weight in shifted_signal.iterrows():
            if weight.sum() == 0.0:
                continue # Skips days with no signal
            returns.append((daily_returns.loc[date] * weight).sum())
            valid_dates.append(date)

        strategy_returns = pd.Series(returns, index = valid_dates)
        results[delay] = strategy_returns

    # print("Max daily return:", strategy_returns.max())
    # print("Min daily return:", strategy_returns.min())
    # print("Top 5 spikes:\n", strategy_returns.sort_values(ascending=False).head())
    return results