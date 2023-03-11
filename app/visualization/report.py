import pandas as pd
import matplotlib.pyplot as plt

class PerformanceReport:
    def __init__(self, backtest):
        self.backtest = backtest
        
    def generate_report(self):
        # Generate trade log
        trade_log = self.backtest.generate_trade_log()
        
        # Generate performance summary
        summary = self.backtest.generate_summary()
        
        # Plot equity curve
        equity_curve = self.backtest.generate_equity_curve()
        plt.plot(equity_curve)
        plt.title('Equity Curve')
        plt.xlabel('Date')
        plt.ylabel('Equity ($)')
        plt.show()
        
        # Print trade log and performance summary
        print('\nTrade Log:')
        print(trade_log)
        
        print('\nPerformance Summary:')
        print(summary)
    