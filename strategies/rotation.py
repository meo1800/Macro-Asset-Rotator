import pandas as pd
from utils.slippage import apply_slippage

def generate_rotation_strategy(assets, window = 21):

    print("\nGenerating strategy...\n")

    # Finding rotation single based on return of trailing window
    trailing_returns = assets.pct_change(periods = window)
    rotation_signal = trailing_returns.dropna().idxmax(axis = 1)

    daily_returns = assets.pct_change().dropna()
    # Realign signal to rotate based on previous days asset and reindex
    aligned_signal = rotation_signal.shift(1).reindex(daily_returns.index).dropna()

    # Calculating the strategy returns based on aligned signal factoring in slippage
    strategy_returns = []
    for date, asset in aligned_signal.items():
        raw_return = daily_returns.loc[date, asset] # No slippage (float)
        slippage_return = apply_slippage(pd.Series([1 + raw_return])).iloc[0] - 1 # Converts float>>list>>series and applies slippage 
        strategy_returns.append(slippage_return)

    # Indexing strategy_returns as a series
    strategy_returns = pd.Series(strategy_returns, index = aligned_signal.index)
   
    return strategy_returns