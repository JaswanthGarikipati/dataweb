
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Hello from Jaswanth G!'

@route('/bye')
def bye_world():
    return 'Bye from Jaswanth G!'

@route('/list')
def get_list():
    return 'The shopping list goes here'

application = default_app()

