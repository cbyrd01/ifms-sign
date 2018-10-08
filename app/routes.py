from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/letter<letter>')
def letter(letter):
    return render_template('letter.html', letter=letter)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/favicon-16x16.png')
def favicon16():
    return app.send_static_file('favicon-16x16.png')

@app.route('/favicon-32x32.png')
def favicon32():
    return app.send_static_file('favicon-32x32.png')