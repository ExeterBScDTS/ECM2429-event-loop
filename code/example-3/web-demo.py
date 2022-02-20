from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''<h1>Homepage</h1>
    <a href="/hello/mike">Hello</a>
    '''

@app.route('/hello/<name>')
def hello(name):
    return f'<b>Hello {name}</b>!'

app.run(host='localhost', port=8080)
