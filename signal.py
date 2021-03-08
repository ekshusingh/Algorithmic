class signal_obv_macd():

    def __init__(self,obv,macd):
        self.obv = obv
        self.macd = macd
        self.signal_list = [0]
        self.buying_price = []
        self.selling_price = []
    def signals(self):
        for i in range(len(self.obv)):
            if self.obv.iloc[i]['CUMSUM'] >= self.obv.iloc[i]['rolling_CUMSUM']  and self.macd.iloc[i]['Slow_macd'] >= self.macd.iloc[i]['Fast_macd']:
                self.signal_list.append('buy')
                self.buying_price.append(self.obv.iloc[i]['Price'])
            elif self.obv.iloc[i]['CUMSUM'] <= self.obv.iloc[i]['rolling_CUMSUM'] and self.signal_list[-1] !='sell' and self.macd.iloc[i]['Slow_macd'] <= self.macd.iloc[i]['Fast_macd']:
                self.signal_list.append('sell')
                self.selling_price.append(self.obv.iloc[i]['Price'])
        
        return self.signal_list,self.selling_price,self.buying_price