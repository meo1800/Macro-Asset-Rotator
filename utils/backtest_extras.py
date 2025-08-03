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
def bl_evaluation_comparison(assets, strategy_results: dict, second_strategy_results: dict = None, third_strategy_results:dict = None):
    
    # Iterates through each delay scenario and evaluates
    for delay, returns in strategy_results.items():
        print(f"\n{delay}d Delay Primary Strategy:\n", evaluate_performance(returns))

    # Allows evaluating an optional second strategy
    if second_strategy_results:
        for delay, returns in second_strategy_results.items():
            print(f"\n{delay}d Delay Secondary Strategy:\n", evaluate_performance(returns))

    # Allows evaluating an optional third strategy
    if third_strategy_results:
        for delay, returns in third_strategy_results.items():
            print(f"\n{delay}d Delay Tertiary Strategy:\n", evaluate_performance(returns))


    baseline_returns = get_base_line_returns(assets)

    print("\nBuy & Hold:\n", evaluate_performance(baseline_returns[0]))
    print("\nEqual Weighted:\n", evaluate_performance(baseline_returns[1]))

# Returns dictionary containing strategies and baselines with respective returns
def total_results_dict(assets, strategy_results: dict, second_strategy_results: dict = None, third_strategy_results:dict = None):
    # Dictionary of labels and return data
    results_dict = {}

    # Loop through each delay scenario of the strategy results dict
    for delay, returns in strategy_results.items():
        label = f"{delay}d Delay Primary Strategy"
        results_dict[label] = returns

    # Allows evaluating an optional second strategy
    if second_strategy_results:
        for delay, returns in second_strategy_results.items():
            label = f"{delay}d Delay Secondary Strategy"
            results_dict[label] = returns

        # Allows evaluating an optional second strategy
    if third_strategy_results:
        for delay, returns in third_strategy_results.items():
            label = f"{delay}d Delay Tertiary Strategy"
            results_dict[label] = returns

    # For comparison     
    results_dict["Buy & Hold"] = get_base_line_returns(assets)[0]
    results_dict["Equal Weighted"] = get_base_line_returns(assets)[1]
    return results_dict