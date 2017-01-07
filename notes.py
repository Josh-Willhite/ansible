from flask import Flask
from boto.s3.connection import S3Connection

s3_conn = S3Connection()
bucket = s3_conn.get_bucket('my-notes')
app = Flask(__name__)

@app.route('/my-notes', defaults={'path': ''})
@app.route('/<path:path>')
def my_notes(path):
    key_path = path.split('/')[1:][0]
    key = bucket.get_key(key_path)
    contents = key.get_contents_as_string()
    return contents

if __name__ == '__main__':
    app.run()
