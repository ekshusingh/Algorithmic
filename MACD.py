import pandas as pd
import numpy as np

class MACD():

    def __init__(self,df,fast_period=20,slow_period=200,period=False):
        self.data = pd.DataFrame(index=df.index)
        self.df = df.reset_index()
        if period:
            self.df = self.df.drop(columns=['Datetime'])
        else:
            self.df = self.df.drop(columns=['Date'])
        self.df = self.df['Close']
        self.fast_period = fast_period
        self.slow_period = slow_period
    
    def macd_return(self,period):
        rolling = self.df.rolling(period).mean()
        return rolling
    
    def macds(self):
        rolling= self.macd_return(self.slow_period)
        self.data['Slow_macd'] = rolling.values
        rolling= self.macd_return(self.fast_period)
        self.data['Fast_macd'] = rolling.values
        return self.data