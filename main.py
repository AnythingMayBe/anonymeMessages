from flask import Flask, render_template, request, redirect
import requests
from werkzeug.exceptions import HTTPException
import re

app = Flask(__name__)
webhookUrl = "" # The webhook URL that will get trigerred.

@app.route("/")
def index():
    return render_template("index.html", error="")

@app.route("/post", methods=["POST"])
def post():
    # Checks
    msg = request.form["message"]

    msg = re.sub("(<[@&].*>)|(@everyone)|(@here)", "<mention>", msg) # Ping-check

    # Send requests
    req = requests.post(webhookUrl, data={"content": msg})
    return redirect("/")

# Error Handler
@app.errorhandler(Exception)
def exception(error):
    if isinstance(error, HTTPException):
        return render_template("index.html", error="Error:" + str(error)), 418
    return render_template("index.html", error="Error: " + str(error)), 500
    
if __name__ == "__main__":
    app.run()