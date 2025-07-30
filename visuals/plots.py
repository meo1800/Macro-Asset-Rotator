import matplotlib.pyplot as plt
import os

#  Standardized plot configuration
plt.rcParams.update({
    "lines.linewidth": 2,
    "axes.grid": True,
    "figure.figsize": (12, 6),
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "legend.fontsize": 11
})

# Plotting function for cumulative returns

def plot_cum_returns(returns_dict: dict):
    fig, ax = plt.subplots()
    for label, returns in returns_dict.items():
        cum_returns = (1 + returns).cumprod()
        ax.plot(cum_returns, label = label)

    # plt.plot(cum_strategy, label = "Rotation Strategy")
    # plt.plot(cum_equal, label = "Equal Weighted", linestyle = "--")
    # plt.plot(cum_spy, label = "Buy&Hold SPY", linestyle = ":")
    ax.set_title("Cumulative Returns")
    ax.set_xlabel("Date")
    ax.set_ylabel("Growth")
    ax.legend()
    fig.tight_layout()
    
    os.makedirs("outputs", exist_ok = 0)
    plt.savefig("outputs/strategy_returns.png")
    plt.close()
    
    return fig