from app import socketio, rdb

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)