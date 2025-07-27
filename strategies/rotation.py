import pandas as pd

def generate_rotation_strategy(assets, window = 21):

    # Finding rotation single based on return of trailing window
    trailing_returns = assets.pct_change(periods = window)
    rotation_signal = trailing_returns.dropna().idxmax(axis = 1)

    daily_returns = assets.pct_change().dropna()
    # Realign signal to rotate based on previous days asset and reindex
    aligned_signal = rotation_signal.shift(1).reindex(daily_returns.index).dropna()

    # Calculating the strategy returns based on aligned signal
    strategy_returns = []
    for date, asset in aligned_signal.items():
        value = daily_returns.loc[date, asset]
        strategy_returns.append(value)

    # Indexing strategy_returns as a series
    strategy_returns = pd.Series(strategy_returns, index = aligned_signal.index)
   
    return strategy_returns