Overview
The trading_simulation project is a web application that simulates trading strategies using historical market data. It allows users to upload a CSV file of historical stock data, select a trading strategy, and run a backtest to see how the strategy would have performed on that data.

Installation
To install the trading_simulation project, first clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/trading_simulation.git
Next, navigate to the project directory and create a virtual environment:

bash
Copy code
cd trading_simulation
python3 -m venv venv
Activate the virtual environment:

bash
Copy code
source venv/bin/activate
Install the required packages:

Copy code
pip install -r requirements.txt
Usage
To start the web application, run the run.py script:

Copy code
python run.py
This will start the web server on http://127.0.0.1:5000/. You can access the application by opening this URL in your web browser.

Uploading data
To upload data, click the "Upload Data" button on the home page. This will take you to a form where you can select a CSV file to upload. The CSV file should have the following columns:

Date: the date of the data point (YYYY-MM-DD format)
Open: the opening price of the stock on that day
High: the highest price of the stock on that day
Low: the lowest price of the stock on that day
Close: the closing price of the stock on that day
Volume: the trading volume for the day
Once you have selected a file, click the "Upload" button to upload it. The file will be stored in the uploads/ directory.

Running a backtest
To run a backtest, click the "Run Backtest" button on the home page. This will take you to a form where you can select the stock you want to backtest, the start and end dates for the backtest, and the trading strategy you want to use.

Once you have selected your options, click the "Run Backtest" button to start the backtest. The results of the backtest will be displayed on the page, along with a chart showing the performance of the trading strategy.

Project structure
The project has the following structure:

markdown
Copy code
trading_simulation/
├── app/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   └── sample_data.csv
│   ├── logic/
│   │   ├── __init__.py
│   │   ├── strategy.py
│   │   ├── signals.py
│   │   └── backtest.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── upload.html
│   │   └── backtest.html
│   ├── uploads/
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── plot.py
│   │   └── report.py
│   ├── routes.py
│   ├── models.py
│   └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_strategy.py
│   └── test_backtest.py
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
``
To config on AWS EC2 for the web server at port 5000, turn on all TCP with all ports in the Security Group. Assign this security group to the EC2. It works as a web server