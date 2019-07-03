from flask import Flask

app = Flask(__name__)

# Probably want to set this up to just be griffin/ with no port number so
# that all of our main stuff goes there. This is where you login and then it
# take you to home page where you can go to all of the other pages needed.
app.config["SERVER_NAME"] = 'localhost:3031'

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"

@app.route('/hello')
def hello():
    return 'Hello, World'