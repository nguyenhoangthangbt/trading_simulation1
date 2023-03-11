from flask import render_template, request, redirect, url_for
from app import app
from app.logic.backtest import Backtest
from app.data.data_loader import DataLoader
import os
from matplotlib import pyplot as plt
import io
import base64

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'sample_data1.csv'))
            return redirect(url_for('backtest'))

    return render_template('upload.html')


from flask import render_template

@app.route('/backtest', methods=['GET', 'POST'])
def backtest():
    # if request.method == 'POST':
    #     # Handle file upload
    #     file = request.files['file']
    #     if file and file.filename.endswith('.csv'):
            
            # m_data_file_path=r'a3_online_platform\app\uploads\sample_data1.csv'#
            m_data_file_path=os.path.join(app.config['UPLOAD_FOLDER'],  'sample_data1.csv')
            # file.save(m_data_file_path)
            backtest = Backtest(m_data_file_path)
            backtest.run()
            total_pnl, total_trades, win_rate, avg_win, avg_loss, max_drawdown, sharpe_ratio = backtest.summary()
            pnl_data = backtest.get_pnl_data()
            # print([total_pnl, total_trades, win_rate, avg_win, avg_loss, max_drawdown, sharpe_ratio])
            return render_template('backtest.html',
                                   total_pnl=total_pnl,
                                   total_trades=total_trades,
                                   win_rate=win_rate,
                                   avg_win=avg_win,
                                   avg_loss=avg_loss,
                                   max_drawdown=max_drawdown,
                                   sharpe_ratio=sharpe_ratio,
                                   pnl_data=pnl_data)
        # else:
            # print('Invalid file format. Please upload a CSV file.')
            # return render_template('backtest.html')
