#!/usr/bin/python3
'''A script that starts a Flask web application with 2 routes'''
from flask import Flask

# create an instance of this class
app = Flask(__name__)


# use route() to tell Flask what URL should trigger our function
@app.route('/', strict_slashes=False)
def hello():
    '''Function to output Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    '''Return HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    '''display “C ” followed by the value of the text variable'''
    return f"C is {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
