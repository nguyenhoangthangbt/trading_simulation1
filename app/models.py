from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class TradingData(db.Model):
    __tablename__ = "trading_data"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ticker = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)

    def __init__(self, ticker, price, volume):
        self.ticker = ticker
        self.price = price
        self.volume = volume

    def __repr__(self):
        return f"<TradingData {self.ticker} {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}>"
