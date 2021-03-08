import pandas as pd
import numpy as np
import yfinance as yf

class ticker_data():
    
    def __init__(self,tickers,period = '5d',interval = '1m' ,start='2019-01-01',end='2021-01-01',want_period=True):
        self.tickers = tickers
        self.period = period
        self.interval = interval
        self.start = start
        self.end = end
        self.want_period = want_period
    def download(self):
        if self.want_period:
            df =yf.download(self.tickers,period=self.period,interval=self.interval)
            
        else:
            df =yf.download(self.tickers,start=self.start,end=self.end)
        df = pd.DataFrame(df,columns=df.columns)
        return df