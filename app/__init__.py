from flask import Flask
from flask_redislite import FlaskRedis
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker
from flask_socketio import SocketIO
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)
rdb = FlaskRedis(app, collections = True)
Bootstrap(app)
colorpicker(app)

from app import routes, sockets

if __name__ == '__main__':
    socketio.run(app)
