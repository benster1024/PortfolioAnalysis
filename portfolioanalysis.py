import yfinance as yf
import pandas as pd
import numpy as np   
import matplotlib.pyplot as plt
#used for linear regression, to find the beta of a stock compared to a benckmark 
import statsmodels.api as sm

portfolio = {
    'AAPL' : 10,
    'TSLA' : 5,
    'MSFT' : 15,
    'GOOGL' : 7
}
benchmark = {
    '^GSPC' : 1
}

start_date = '2023-01-01'
end_date = '2024-01-01'

def ShowBasicGraph(data):
    #plot the adjusted close prices over the specified start and end dates
    data.plot()
    plt.show()

def GetData(data):
#grab the adjusted close price of all stocks in my portfolio
    data = yf.download(list(data.keys()), start=start_date, end=end_date,interval="3mo")['Adj Close']
    return data
    
def main():
    data= GetData(portfolio)
    quaterly_returns = data.pct_change()
    quaterly_cum_returns = (quaterly_returns+1).cumprod()
    quaterly_cum_returns = quaterly_cum_returns.dropna(axis=0)
    print(quaterly_cum_returns)
main()
