from flask import Flask

app = Flask(__name__)

@app.route("/") #para crear la url 

def hello_world():
    return "Hello, World"