import matplotlib.pyplot as plt

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
    fig, ax = plt.subplot()
    for label, returns in returns_dict:
        cum_returns = (1 + returns).cumprod()
        ax.plot(cum_returns, label = label)

    # plt.plot(cum_strategy, label = "Rotation Strategy")
    # plt.plot(cum_equal, label = "Equal Weighted", linestyle = "--")
    # plt.plot(cum_spy, label = "Buy&Hold SPY", linestyle = ":")
    ax.title("Cumulative Returns")
    ax.xlabel("Date")
    ax.ylabel("Growth")
    ax.legend()
    ax.tight_layout()
    plt.show()
    return fig