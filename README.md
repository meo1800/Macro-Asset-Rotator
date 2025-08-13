## Macro Asset Rotator

A Python-based backtesting framework for rotating between macro assets (e.g., SPY, IEF, GLD) using trailing return-based signals. The project compares the performance of a 3 different strategies against Buy & Hold and Equal Weighted benchmarks.

## Features

- **Rotation Strategies**: Trailing return–based rotation across multiple assets
- **Benchmarks**: Buy & Hold and Equal Weighted
- **Performance Metrics**:
  - Total Return
  - Annualized Return & Volatility
  - Sharpe Ratio
  - Max Drawdown
- **Clean Modular Codebase**: Easy to extend with new strategies or metrics
- **Visualization**: Cumulative return plotting for quick performance review
- **Summary Output**: CSV file with detailed performance metrics for all strategies

## Project Structure

```text
Macro-Asset-Rotator/
├── data/
│   ├── fetch.py                  # Data retrieval using Alpha Vantage
│   ├── GLD.csv
│   ├── IEF.csv                   # Cached asset information
│   └── SPY.csv
├── metrics/
│   └── performance.py            # Performance evaluation tools
├── notebooks/
│   ├── asset_rotation_strategy.ipynb
│   └── single_asset_SMA_strategy.ipynb
├── outputs/
│   ├── strategy_returns.png      # Cumulative returns chart
│   └── strategy_summary.csv      
├── strategies/
│   ├── multi_signal.py
│   ├── rotation.py               # Rotation logic
│   └── top_performers.py
├── utils/
│   ├── backtest_extras.py
│   ├── slippage.py
│   └── plots.py
├── env/                          
├── backtest.py                   # Main execution script
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/macro-asset-rotator.git
cd macro-asset-rotator
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3.	Add your Alpha Vantage API key in data/fetch.py.

4.  Run the backtest:
```bash
python3 bactkest.py
```

Results will be saved in:
-   outputs/strategy_returns.png — Cumulative returns chart
-   outputs/strategy_summary.csv — Performance metrics table