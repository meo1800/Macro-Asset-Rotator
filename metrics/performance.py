import numpy as np
import pandas as pd

def evaluate_performance(returns, rfr = 0):
    results = {}
    cum = (1 + returns).cumprod()
    results["Total Return"] = cum.iloc[-1] - 1 
    results["Annualized Volatility"] = returns.std() * np.sqrt(252)
    results["Annualized Return"] = (1 + results["Total Return"])**(252 / len(returns)) - 1
    results["Sharpe Ratio"] = ((returns.mean() - (rfr / 252)) / returns.std()) * np.sqrt(252)
    
    # Biggest loss experienced
    cum_max = cum.cummax()
    drawdown = cum / cum_max - 1
    results["Max Drawdown"] = drawdown.min()

    return pd.Series(results)