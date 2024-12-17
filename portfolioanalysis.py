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

start_date = '2020-01-01'
end_date = '2022-01-03'

def ShowBasicGraph(data):
    #plot the adjusted close prices over the specified start and end dates
    data.plot()
    plt.show()

def GetData(data):
    """
    grabs the adjusted close price of all stocks in my portfolio
    from yahoo finance
    """
    data = yf.download(list(data.keys()), start=start_date, end=end_date,interval="1d")['Adj Close']
    return data

def QuaterlyReturns(data):
    """Generates the cumalative quaterly returns of a set of stock
    if AAPL had a .17 cumaltive return on 2023-10-01, then we know that the
    stock grew by 17% from to any given start date to 2023-10-01
    """
    quaterly_returns = data.pct_change()
    quaterly_cum_returns = (quaterly_returns+1).cumprod() - 1
    quaterly_cum_returns = quaterly_cum_returns.dropna(axis=0)
    return quaterly_cum_returns  

def Volatility(data):
    #takes the annualized daily volatility of everything in the portfolio,
    #assumes the prices movements scale linearly with time
    data = GetData(data)
    returns = data.pct_change()
    volatility = returns.std()
    annualized_vol = volatility * np.sqrt(252)
    return annualized_vol * 100
def main():
    
    print(Volatility(portfolio))
    

    
main()
 