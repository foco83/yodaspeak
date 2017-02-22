# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import unirest
import requests

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/yoda/")
def yoda_speak():
    sentence = request.args.get("sentence")
    yodasentence(sentence)

    return render_template("yoda.html",sentence=sentence)

def yodasentence(sentence):

    response = unirest.get("https://yoda.p.mashape.com/yoda?sentence=" + sentence.replace(" ","+"), headers={"X-Mashape-Key": "92thM2G2kWmshQoT17QNg4gfaAvbp1Yuv31jsnbNMeCybOJXUE","Accept": "text/plain"})
    print(response.code)
    print(response.body)



if __name__ == "__main__":
    app.run(debug=True)
