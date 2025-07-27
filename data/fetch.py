from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

# Defining get asset data variable from Alpha Vantage
def get_asset_data(symbol):
    filepath = f"data/{symbol}.csv"

    # Uses cached data if same ticker was used before
    if os.path.exists(filepath):
        print(f"Loading {symbol} from cache... ")
        df = pd.read_csv(filepath, index_col = 0, parse_dates = True)
        df.columns = [symbol]
        return df.sort_index()
    
    # If not cached, use Alpha Vantage
    print(f"Fetching {symbol} from Alpha Vantage... ")
    ts = TimeSeries(key = api_key, output_format = "pandas") # Activates API and sets outpout format to pandas
    data, _ = ts.get_daily(symbol = symbol, outputsize = "full")
    data = data[['4. close']] # DF becoems just the close column
    data.columns = [symbol] 
    data.index = pd.to_datetime(data.index) # Converts index from data strings to date/time objects
    return data.sort_index() 

# Uses list of tickers to return a dataframe of given assets' close prices
def generate_assets_df(tickers):
    # Creates dictionary of single column df's for each ticker
    data = {}

    for symbol in tickers:
        print(f"Getting data for {symbol}")
        asset_df = get_asset_data(symbol)
        data[symbol] = asset_df

    # Concatenates the data for each ticker into one data frame
    assets = pd.concat(data.values(), axis = 1)
    assets.dropna(inplace = True)
    return assets