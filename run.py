from flask import Flask, render_template
import os
import random
import urllib.request, json

# http://getskeleton.com/
# https://opentdb.com/api_config.php

def genKey():
    """
    This function Generates a random value to be used as the key for a test access code
    :return:
    """
    return random.randint(1,2000000)

def getQuestions(qty):
    baseUrl = "https://opentdb.com/api.php?amount=10"
    specificUrl = "https://opentdb.com/api.php?amount=10&category=29&difficulty=medium"
    with urllib.request.urlopen(baseUrl) as url:
        data = json.loads(url.read().decode())
        print(data)


print(f"Current Working Directory = {os.getcwd()}")
os.chdir(".")
print(os.getcwd())
app = Flask(__name__)

@app.route("/")
def index():
    greetings = """QUIZLET from OSU...
    This app is expressly for the purpose of getting an A
    in our Capstone Project"""
    test2 = "way too much fun....."
    ccValue = "349950727078541"
    test2 = genKey()
    test3 = genKey()
    return render_template("home.html", greetings=greetings, dobie=test2, dibs=test3)


@app.route("/about")
def index2():
    greetings = """QUIZLET from OSU...
    This app is expressly for the purpose of getting an A
    in our Capstone Project"""
    detail = " Please Vote with your usage.... the more hits the better...."

    return render_template("homie2.html", greetings=greetings, detail=detail)


@app.route("/help")
def index3():
    greetings = """...HELP, HELP, HELP..."""

    detail = "All the help you will ever need"

    return render_template("homie2.html", greetings=greetings, detail=detail)


@app.route("/contact")
def index4():
    greetings = """...CONTACT..."""

    detail = "All the touch you will ever need"

    return render_template("homie2.html", greetings=greetings, detail=detail)


@app.route("/client")
def index5():
    greetings = """...CLIENT..."""

    detail = "All the QUESTIONS you will ever need"

    return render_template("homie2.html", greetings=greetings, detail=detail)


if __name__ == "__main__":
    app.directory = './'
    app.run(host='127.0.0.1', port=5000)