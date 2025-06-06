from flask import Flask
from config import *
app = Flask(__name__)
app.config.from_pyfile('config.py')