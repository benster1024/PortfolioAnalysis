import yfinance as yf
import pandas as pd
import numpy as np   
import matplotlib.pyplot as plt

portfolio = {
    'AAPL' : 10,
    'TSLA' : 5,
    'MSFT' : 15,
    'GOOGL' : 7
}

start_date = '2023-01-01'
end_date = '2024-01-01'
appl = yf.Ticker("aapl")
appl