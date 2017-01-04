from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'root path'

@app.route('/notes', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'requested path: {}'.format(path)

if __name__ == '__main__':
    app.run()
