
#Step1: Importing Package
from  flask import Flask

#Step2: Creating an Object (Double Underscore - DunDer)
myApp = Flask(__name__)

#Define route
@myApp.route('/')
def display():
    return 'Hello World'



@myApp.route('/ContactUs')
def contactus():
    return '<h1> You are visiting Contact Us page </h1>'

@myApp.route('/Name/<name>')
def name(name):
    return'Welcome %s as a Guest '%name

if __name__ == '__main__':
   myApp.run(debug = True)


