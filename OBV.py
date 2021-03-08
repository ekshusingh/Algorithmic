import pandas as pd
import numpy as np

class OBV():

    def __init__(self,df,period=False):
        self.data = pd.DataFrame(index=df.index)
        self.df = df.reset_index()
        if period:
            self.df = self.df.drop(columns=['Datetime'])
        else:
            self.df = self.df.drop(columns=['Date'])

    def obvs(self):
        self.df['direction'] = np.where(self.df['Close']>self.df['Close'].shift(1),1,-1)
        self.df['direction * volume'] = self.df['Volume'] * self.df['direction']
        self.df['direction * volume'].iloc[0] = self.df['Volume'].iloc[0]
        self.data['Price'] = self.df['Close'].values
        self.data['CUMSUM'] = self.df['direction * volume'].cumsum().values
        self.data['rolling_CUMSUM'] = self.data['CUMSUM'].rolling(20).mean().values
        return self.data