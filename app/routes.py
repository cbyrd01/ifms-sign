from flask import render_template
from app import app, rdb

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/letter<letter>')
def letter(letter):
    collection = rdb.collection
    letter_values = collection.dict(letter)
    letter_values['red'] = 255
    letter_values['green'] = 32
    letter_values['blue'] = 128
    return render_template('letter.html', letter=letter, red_val=letter_values['red'], green_val=letter_values['green'], blue_val=letter_values['blue'])

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/favicon-16x16.png')
def favicon16():
    return app.send_static_file('favicon-16x16.png')

@app.route('/favicon-32x32.png')
def favicon32():
    return app.send_static_file('favicon-32x32.png')
