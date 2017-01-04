from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! test!'

@app.route('/notes')
def hello_notes():
    return 'these are notes'

if __name__ == '__main__':
    app.run()
