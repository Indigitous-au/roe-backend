import common
from flask import request

app = common.app

@app.route('/')
def root():
    return 'hello'

# receive stuff from button, save to server
@app.route('/button_input', methods=['POST'])
def receive_from_button():
    # get input fields from button
    # post onto server
    pass