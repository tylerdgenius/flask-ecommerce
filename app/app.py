from flask import Flask
from .routes import register_routes
from .database import db
from app.load_data import load_data
from flask_bootstrap import Bootstrap 

app = Flask(__name__, static_folder=None)

app.static_url_path = ""

Bootstrap(app)

app.config.from_pyfile('./config.py')

app.secret_key = app.config['SECRET_KEY']

db.init_app(app)

with app.app_context():

    db.create_all()

    load_data()

register_routes(app)