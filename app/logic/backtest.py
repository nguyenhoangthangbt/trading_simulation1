import pandas as pd
import talib as ta
import numpy as np


class Backtest:
    def __init__(self, data_path, fast_ma=10, slow_ma=20, commission=0.0, swap=0.0):
        self.data = pd.read_csv(data_path)
        self.data.columns = self.data.columns.str.capitalize()
        self.fast_ma = fast_ma
        self.slow_ma = slow_ma
        self.commission = commission
        self.swap = swap
        
        self.signals = None
        self.positions = None
        self.pnl = None
        
    def run(self):
        # Calculate moving averages
        self.data['fast_ma'] = ta.SMA(self.data['Close'], self.fast_ma)
        self.data['slow_ma'] = ta.SMA(self.data['Close'], self.slow_ma)

        # Generate trading signals
        self.signals = np.zeros_like(self.data['Close'])
        self.signals[self.fast_ma:] = np.where(
            self.data['fast_ma'][self.fast_ma:] > self.data['slow_ma'][self.fast_ma:], 1.0, 0.0
        )

        # Calculate positions and P&L
        self.positions = np.concatenate(([0], np.diff(self.signals)))
        self.pnl = self.positions * self.data['Close'] - (self.commission + self.swap)
        # print(self.pnl)
        
    def summary(self):
        total_trades = len(self.pnl[self.pnl != 0])
        win_trades = len(self.pnl[self.pnl > 0])
        loss_trades = len(self.pnl[self.pnl < 0])
        win_rate = win_trades / total_trades
        avg_win = self.pnl[self.pnl > 0].mean()
        avg_loss = self.pnl[self.pnl < 0].mean()
        total_pnl = self.pnl.sum()
        max_drawdown = (self.pnl.cumsum().cummax() - self.pnl.cumsum()).max()
        sharpe_ratio = self.pnl.mean() / self.pnl.std() * np.sqrt(252)
        
        print(f"Total P&L: {total_pnl:.2f}")
        print(f"Total Trades: {total_trades}")
        print(f"Win Rate: {win_rate:.2%}")
        print(f"Avg. Win: {avg_win:.2f}")
        print(f"Avg. Loss: {avg_loss:.2f}")
        print(f"Max Drawdown: {max_drawdown:.2f}")
        print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
        return total_pnl, total_trades, win_rate, avg_win, avg_loss, max_drawdown, sharpe_ratio
        
    def get_pnl_data(self):
        
        return self.pnl.tolist()
