from app import socketio, rdb


@socketio.on('letterF')
def handle_letterF(message):
    collection = rdb.collection
    letter_values = collection.dict("letters")
    letter_values['F'] = message
    socketio.emit('letterF', message, broadcast=True)
    print('letterF' + message)

@socketio.on('letterO')
def handle_letterO(message):
    collection = rdb.collection
    letter_values = collection.dict("letters")
    letter_values['O'] = message
    socketio.emit('letterO', message, broadcast=True)
    print('letterO' + message)

@socketio.on('letterR')
def handle_letterR(message):
    collection = rdb.collection
    letter_values = collection.dict("letters")
    letter_values['R'] = message
    socketio.emit('letterR', message, broadcast=True)
    print('letterR' + message)

@socketio.on('letterG')
def handle_letterG(message):
    collection = rdb.collection
    letter_values = collection.dict("letters")
    letter_values['G'] = message
    socketio.emit('letterG', message, broadcast=True)
    print('letterG' + message)

@socketio.on('letterE')
def handle_letterE(message):
    collection = rdb.collection
    letter_values = collection.dict("letters")
    letter_values['E'] = message
    socketio.emit('letterE', message, broadcast=True)
    print('letterE' + message)