from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    pass

@app.route("/post")
def post():
    pass

app.run()