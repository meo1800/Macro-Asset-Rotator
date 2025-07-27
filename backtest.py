import pandas as pd

from data.fetch import get_asset_data
from strategies.rotation import generate_rotation_strategy
from metrics.performance import evaluate_performance

# Defining tickers
tickers = ["SPY", "IEF", "GLD"]


# Creates dictionary of single column df's for each ticker
data = {}

for symbol in tickers:
    print(f"Getting data for {symbol}")
    asset_df = get_asset_data(symbol)
    data[symbol] = asset_df

# Concatenates the data for each ticker into one data frame
assets = pd.concat(data.values(), axis = 1)

assets.dropna(inplace = True)

print(assets.tail())
