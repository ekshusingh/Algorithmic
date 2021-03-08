import pandas as pd
import numpy as np

class bollinger_bands():

    def __init__(self,df,period=False):
        self.data = pd.DataFrame(index=df.index)
        self.df = df.reset_index()
        if period:
            self.df = self.df.drop(columns=['Datetime'])
        else:
            self.df = self.df.drop(columns=['Date'])
        self.df = self.df['Close']
        
    def standard_dev(self):
        stdev = self.df.std()
        return stdev
    def bands(self):
        self.data['Band_upper'] = (self.df +  self.standard_dev()).values
        self.data['Band_lower'] = (self.df - self.standard_dev()).values
        return self.data
