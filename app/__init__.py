from flask import Flask
from flask_redislite import FlaskRedis
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
rdb = FlaskRedis(app, collections = True)
Bootstrap(app)

from app import routes
