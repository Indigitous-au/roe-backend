import common

app = common.app

@app.route('/')
def root():
    return 'hello'