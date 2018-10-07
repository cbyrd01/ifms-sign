# ifms-sign
Python-Flask interface for Inventor Forge Makerspace sign

## Requirements
Python3 (tested on Python 3.6.6)

## Installation
The following commands set up a Python3 virtual environment and install dependencies:
```
$ git clone https://github.com/cbyrd01/ifms-sign.git
$ cd ifms-sign
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Running Development
The following commands will run a development server. Please note that this is unsafe for production use.
```
$ source venv/bin/activate
(venv) $ export FLASK_APP=sign
(venv) $ export FLASK_ENV=development
(venv) $ flask run
```
