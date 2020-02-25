    
# lets crete a function to calculculate sharpe ratio 
def sharpe_ratio(returns,risk_free_rate = 0.06):
    import numpy as np 
    ret = returns.mean() * 252
    vol  = returns.std() * np.sqrt(252)
    
    # formula for sharpe is preety simple 
    # (returns - risk_free_rate)/ std_of_returns
    sharpe = (ret - risk_free_rate)/vol
    
    return sharpe 
    
    
def CAGR(returns):
    returns = returns.to_frame()
    returns["cum_returns"] = (1 + returns).cumprod()
    years = len(returns)/252
    cagr = (returns["cum_returns"][-1]) ** (1/years) - 1
    return cagr



    
# lets create a function to calculate 
def volitlity(returns,period = 252):
    import numpy as np 
    # lets get the mean std and muliply that with sqaure root of time 
    vol = returns.std() * np.sqrt(period)
    return vol
    
    
    
def drawdown(returns):
    import numpy as np 
    df = returns.to_frame()
    df["Daily_returns"] = df.iloc[:,0]
    df["cumalative_returns"] = (1 + df.Daily_returns).cumprod()

    df["rolling_max"] = df.cumalative_returns.cummax()
    df["drawdown"] = (df.rolling_max - df.cumalative_returns)
    df["drawdown_pct"] = df.drawdown/df.rolling_max

    return df.drawdown_pct.max()


# lets create a function to caculate sortino ratio 
def sortino_ratio(returns,risk_free_rate = 0.06):
    import numpy as np 
    # getting mean of returns 
    ret = returns.mean() * 252
    
    # getting std of only negative returns 
    neg_returns = pd.Series(list(filter(lambda x: x < 0,returns)))
    neg_vol = neg_returns.std() * np.sqrt(252)
    
    sortino = (ret - risk_free_rate)/neg_vol
    
    return sortino
    
    