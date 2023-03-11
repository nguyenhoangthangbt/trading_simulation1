import talib
import numpy as np
import pandas as pd

class SimpleMovingAverageStrategy:
    def __init__(self, data, period):
        self.data = data
        self.period = period
        
    def generate_signals(self):
        close_prices = np.array(self.data['close'])
        sma = talib.SMA(close_prices, timeperiod=self.period)
        signals = pd.DataFrame(index=self.data.index)
        signals['buy'] = np.where(close_prices > sma, 1.0, 0.0)
        signals['sell'] = np.where(close_prices < sma, 1.0, 0.0)
        return signals
