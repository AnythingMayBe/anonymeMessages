from flask import Flask, render_template, request, redirect
import requests
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
webhookUrl = "" # The webhook URL that will get trigerred.

@app.route("/")
def index():
    return render_template("index.html", error="")

@app.route("/post", methods=["POST"])
def post():
    req = requests.post(webhookUrl, data={"content": request.form["message"]})
    return redirect("/")

# Error Handler
@app.errorhandler(Exception)
def exception(error):
    if isinstance(error, HTTPException):
        return render_template("index.html", error="Error:" + str(error)), 418
    return render_template("index.html", error="Error: " + str(error)), 500

app.run()