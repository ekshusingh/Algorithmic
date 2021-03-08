import pandas as pd
import numpy as np

class ATR():

    def __init__(self,df,num_period=20,period=False):
        self.data = pd.DataFrame(index=df.index)
        self.df = df.reset_index()
        if period:
            self.df = self.df.drop(columns=['Datetime'])
        else:
            self.df = self.df.drop(columns=['Date'])
    
    def atrs(self): 
        self.data['high-low'] = (self.df['High'] - self.df['Low']).values
        self.data['high-close'] = (self.df['High'] - self.df['Close'].shift(1)).values
        self.data['low-close'] = (self.df['Low'] - self.df['Close'].shift(1)).values
        self.data['TR'] = np.max(self.data,axis=1)
        self.data['ATR'] = self.data['TR'].rolling(20).mean().values
        return self.data['ATR']