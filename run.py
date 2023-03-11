from app import app, routes


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# if True:
#     # os.path.join(app.config['UPLOAD_FOLDER'],  'sample_data1.csv')
#     m_data_file_path = r'a3_online_platform\app\uploads\sample_data1.csv'
#     backtest = routes.Backtest(m_data_file_path)
#     backtest.run()
#     total_pnl, total_trades, win_rate, avg_win, avg_loss, max_drawdown, sharpe_ratio = backtest.summary()
#     pnl_data = backtest.get_pnl_data()
#     print([total_pnl, total_trades, win_rate, avg_win,
#           avg_loss, max_drawdown, sharpe_ratio])