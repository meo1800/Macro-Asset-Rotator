import pandas as pd

def get_base_line_returns(assets):
    # Find Buy & Hold SPY and equal weighted portfolio returns for comparison
    buy_and_hold_returns = assets["SPY"].pct_change().dropna()
    equal_weighted_returns = assets.pct_change().dropna().mean(axis = 1)
    return buy_and_hold_returns, equal_weighted_returns

