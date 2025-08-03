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
    
    summary_data = []

    # Iterates through each delay scenario and evaluates
    for delay, returns in strategy_results.items():
        metrics = evaluate_performance(returns)
        summary_data.append({
            "Strategy": "Primary Strategy",
            "Delay": delay,
            **metrics.to_dict()
        })

    # Allows evaluating an optional second strategy
    if second_strategy_results:
        for delay, returns in second_strategy_results.items():
            metrics = evaluate_performance(returns)
            summary_data.append({
                "Strategy": "Secondary Strategy",
                "Delay": delay,
                **metrics.to_dict()
            })

    # Allows evaluating an optional third strategy
    if third_strategy_results:
        for delay, returns in third_strategy_results.items():
            metrics = evaluate_performance(returns)
            summary_data.append({
                "Strategy": "Tertiary Strategy",
                "Delay": delay,
                **metrics.to_dict()
            })

    baseline_returns = get_base_line_returns(assets)

    # Appends Buy and Hold metrics to summary
    summary_data.append({
        "Strategy": "Buy and Hold",
        "Delay": 0,
        **evaluate_performance(baseline_returns[0]).to_dict()
    })


    # Appends Equal Weighted Portfolio metrics to summary
    summary_data.append({
        "Strategy": "Equal Weighted",
        "Delay": 0,
        **evaluate_performance(baseline_returns[1]).to_dict()
    })

    # Creates a Metrics Summary DF and updates it to a CSV 
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv("outputs/strategy_summary.csv", index=False)
    print("\nSummary saved to outputs/strategy_summary.csv")
    print(summary_df.to_string(index = False))

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