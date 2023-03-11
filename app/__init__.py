from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.template_folder = app.config['TEMPLATE_FOLDER']

# Import routes
from app import routes
