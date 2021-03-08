from MACD import MACD
from OBV import OBV
from Bands import bollinger_bands
from ATR import ATR
from finance_data import ticker_data
import matplotlib.pyplot as plt
from statistics import mean
from signal import signal_obv_macd
from collections import Counter
df = ticker_data('GRANULES.NS',start='2008-01-01',end='2021-01-01',want_period=False).download()

atr = ATR(df).atrs()

bands = bollinger_bands(df,period=False).bands()

macd = MACD(df,20,200).macds()

obv = OBV(df).obvs()

signals,selling_price,buying_price = signal_obv_macd(obv,macd).signals()

