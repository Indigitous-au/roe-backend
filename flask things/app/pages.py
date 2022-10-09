from flask import request
from receive_request import from_request
from connect_to_database import to_database
from app import app

@app.route('/')
def root():
    return 'hello'

# receive stuff from button, save to server
#TODO make it work for post requests
@app.route('/button_input', methods=['GET','POST'])
def receive_from_button():
    # get input fields from button
    data = from_request(request)
    # post onto server
    to_database(data)
    return "received"