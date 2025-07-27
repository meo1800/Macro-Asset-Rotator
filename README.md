## Macro Asset Rotator

A Python-based backtesting framework for rotating between macro assets (e.g., SPY, IEF, GLD) using trailing return-based signals. The project compares the performance of a rotation strategy against Buy & Hold and Equal Weighted benchmarks.

## Features

- Asset rotation strategy based on trailing returns
- Performance metrics: total return, volatility, Sharpe ratio, and max drawdown
- Benchmark comparison: Buy & Hold and Equal Weighted
- Cumulative return plotting
- Modular codebase for easy extension

## Project Structure

```text
Macro-Asset-Rotator/
├── backtest.py              # Main execution script
├── data/
│   └── fetch.py             # Data retrieval using Alpha Vantage
├── strategies/
│   └── rotation.py          # Rotation logic
├── metrics/
│   └── performance.py       # Performance evaluation tools
├── visuals/
│   └── plots.py             # Cumulative return plotting
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

