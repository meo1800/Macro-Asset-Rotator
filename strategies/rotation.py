import pandas as pd
from utils.slippage import apply_slippage

# Incorporates simulated alpha decay and slippage returning a dictionary with returns of each delay scenario
def generate_rotation_strategy(assets, window = 21, max_delay = 3):

    print("\nGenerating strategy...\n")

    # Finding rotation single based on return of trailing window
    trailing_returns = assets.pct_change(periods = window)
    rotation_signal = trailing_returns.dropna().idxmax(axis = 1)
    daily_returns = assets.pct_change().dropna()

    # Stores return series for each level of delay
    decay_results = {}

    # Simulates performance for each delay in the range
    for delay in range(1, max_delay + 1):

        # Shifts the trade signal by delay
        shifted_signal = rotation_signal.shift(delay)

        # Ensures that there are not missing dates and that the index is realigned to return data
        aligned_signal = shifted_signal.reindex(daily_returns.index).dropna()

        # # Check for top contributors
        # print(aligned_signal.value_counts())

        # Calculating the strategy returns based on aligned signal factoring in slippage
        strategy_returns = []
        current_asset = None 

        for date, asset in aligned_signal.items():

            # Ensures any NaNs do not cause the entire backtest to fail 
            try:
                # Ensures trading is only done when asset changes and not when held
                if current_asset is None or asset != current_asset:
                        
                    raw_return = daily_returns.loc[date, asset] # No slippage (float)
                    slippage_return = apply_slippage(pd.Series([1 + raw_return])).iloc[0] - 1 # Converts float>>list>>series and applies slippage 
                    strategy_returns.append(slippage_return)
                    current_asset = asset
                else: 
                    # Continue holding the same asset (no trades)
                    held_return = daily_returns.loc[date, current_asset]
                    strategy_returns.append(held_return)

            except KeyError:
                continue

        # Indexing strategy_returns as a series
        strategy_returns = pd.Series(strategy_returns, index = aligned_signal.index)
        decay_results[delay] = strategy_returns
   
    return decay_results
