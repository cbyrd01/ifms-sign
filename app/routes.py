from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html', title='IFMS Sign')

@app.route('/letterF')
def letterF():
    return render_template('letterF.html', title='IFMS Sign')

@app.route('/letterO')
def letterO():
    return render_template('letterO.html', title='IFMS Sign')

@app.route('/letterR')
def letterR():
    return render_template('letterR.html', title='IFMS Sign')

@app.route('/letterG')
def letterG():
    return render_template('letterG.html', title='IFMS Sign')

@app.route('/letterE')
def letterE():
    return render_template('letterE.html', title='IFMS Sign')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/favicon-16x16.png')
def favicon16():
    return app.send_static_file('favicon-16x16.png')

@app.route('/favicon-32x32.png')
def favicon32():
    return app.send_static_file('favicon-32x32.png')