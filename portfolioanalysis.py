import yfinance as yf
import pandas as pd
import numpy as np   
import matplotlib.pyplot as plt
#used for linear regression, to find the beta of a stock compared to a benckmark 
import statsmodels.api as sm

portfolio = {
   
}
benchmark = {
    '^GSPC' : 1
}

def get_user_portfolio(portfolio_name):
    print("Enter 'done' as the Ticke when you're finished.\n")
    
    user_dict = {}
    while True:
        key = input("Enter Ticker (or 'done' to stop): ")
        if key.lower() == 'done':
            break
        value = input(f"Enter amount of shares for '{key}': ")
        user_dict[key] = value
    return user_dict

def get_user_benchmark(benchmark):
    user_dict = {}
    key = input("Enter Benchmark's Ticker")
    user_dict[key] = 1
    return user_dict

start_date = '2020-01-01'
end_date = '2022-04-01'

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
    inputted = get_user_portfolio(portfolio)
    data = GetData(inputted)
    print(data)

    
main()
 