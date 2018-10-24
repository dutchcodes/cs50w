from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    randomvariable = "Adjust this"
    return "Hello World!"

@app.route("/<string:name>")
def hello(name):
    return f"Hello motherfucking {name}!"
