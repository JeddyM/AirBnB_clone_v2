#!/usr/bin/python3
'''A script that starts a Flask web application with 6 routes'''
from flask import Flask
from flask import render_template

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
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is cool"):
    '''display python followed by the value of the text variable
    replace underscore _ symbols with a space
    The default value of text is “is cool”
    '''
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    '''Display “n is a number” only if n is an integer'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    '''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
