import pandas as pd
from metrics.performance import evaluate_performance

# Returns a list containing returns of Buy & Hold [0] and Equal Weighted [1] as baselines 
def get_base_line_returns(assets):
    # Find Buy & Hold SPY and equal weighted portfolio returns for comparison
    buy_and_hold_returns = assets["SPY"].pct_change().dropna()
    equal_weighted_returns = assets.pct_change().dropna().mean(axis = 1)
    baseline_returns = [buy_and_hold_returns, equal_weighted_returns]
    return baseline_returns

# Evaluates performance of the strategy with each delay scenario with comparison to baseline returns
def bl_evaluation_comparison(strategy_returns: dict, assets, second_strategy_returns: dict = None):
    
    # Iterates through each delay scenario and evaluates
    for delay, returns in strategy_returns.items():
        print(f"\n{delay}d Delay Primary Strategy:\n", evaluate_performance(returns))

    # Allows evaluating an optional second strategy
    if second_strategy_returns:
        for delay, returns in second_strategy_returns.items():
            print(f"\n{delay}d Delay Secondary Strategy:\n", evaluate_performance(returns))


    baseline_returns = get_base_line_returns(assets)

    print("\nBuy & Hold:\n", evaluate_performance(baseline_returns[0]))
    print("\nEqual Weighted:\n", evaluate_performance(baseline_returns[1]))