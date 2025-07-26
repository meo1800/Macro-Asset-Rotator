from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

# Defining get asset data variable from Alpha Vantage
def get_asset_data(symbol):
    ts = TimeSeries(key = api_key, output_format = "pandas") # Activates API and sets outpout format to pandas
    data, _ = ts.get_daily(symbol = symbol, outputsize = "full")
    data = data[['4. close']] # DF becoems just the close column
    data.columns = [symbol] 
    data.index = pd.to_datetime(data.index) # Converts index from data strings to date/time objects
    return data.sort_index() 
