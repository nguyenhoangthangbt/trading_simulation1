# app/logic/signals.py

import pandas as pd

class Signals:
    def __init__(self, data, strategy):
        self.data = data
        self.strategy = strategy
        self.signals = pd.DataFrame()

    def generate_signals(self):
        self.signals = self.strategy.generate_signals(self.data)

    def get_trades(self):
        trades = pd.DataFrame()
        pos = 0
        direction = 0
        for i in range(len(self.signals)):
            signal = self.signals.iloc[i]
            if signal['signal'] == 1 and pos == 0:
                pos = signal['close']
                direction = 1
            elif signal['signal'] == -1 and pos == 0:
                pos = signal['close']
                direction = -1
            elif signal['signal'] == -1 and pos > 0:
                trades = trades.append({'open': pos, 'close': signal['close'], 'direction': direction}, ignore_index=True)
                pos = 0
                direction = 0
            elif signal['signal'] == 1 and pos < 0:
                trades = trades.append({'open': pos, 'close': signal['close'], 'direction': direction}, ignore_index=True)
                pos = 0
                direction = 0
