from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
webhookUrl = "" # The webhook URL that will get trigerred.

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post", methods=["POST"])
def post():
    req = requests.post(webhookUrl, data={"content": request.form["message"]})
    return redirect("/")

app.run()