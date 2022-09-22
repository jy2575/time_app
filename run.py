from flask import Flask
from time import localtime, strftime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def show_currrent_time():
    return strftime("%H:%M:%S", localtime())


app.run(host='0.0.0.0', port=8080, debug=True)
