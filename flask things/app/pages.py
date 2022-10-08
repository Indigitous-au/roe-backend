from flask import request
from parser import from_request
from database import to_database
from app import app

@app.route('/')
def root():
    return 'hello'

# receive stuff from button, save to server
@app.route('/button_input')
def receive_from_button():
    print(request)
    # get input fields from button
    data = from_request(request)
    # post onto server
    to_database(data)
    return "received"