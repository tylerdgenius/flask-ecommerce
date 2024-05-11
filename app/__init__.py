from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import register_routes
from .products import products

app = Flask(__name__, static_folder=None)
app.config.from_pyfile('../config.py')

db = SQLAlchemy(app)

register_routes(app)