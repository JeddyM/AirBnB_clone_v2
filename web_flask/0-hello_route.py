#!/usr/bin/python3
'''A script that starts a Flask web application'''
from flask import Flask

# create an instance of this class
app = Flask(__name__)


# use route() to tell Flask what URL should trigger our function
@app.route('/', strict_slashes=False)
def hello():
    '''Function to output Hello HBNB!'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
