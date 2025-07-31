import numpy as np
import pandas as pd

# Simulates slippage by pulling from a normal distribution with mean of 5 bps and std of 2 bps
def apply_slippage(price_series, mean_slip = 0.0005, std_slip = 0.0002):
    slip_pct = np.random.normal(loc = mean_slip, scale = std_slip, size = len(price_series))
    return price_series * (1 - slip_pct)

