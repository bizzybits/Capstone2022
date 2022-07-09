from models import db, QuestionModel
from flask import Flask, render_template, request, redirect
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


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quizgame.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


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


# CREATE VIEW
@app.route("/questions/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("createquestion.html")

    if request.method == "POST":
        question_id = request.form["question_id"]
        question_text = request.form["question"]
        answer = request.form["answer"]
        question = QuestionModel(
            question_id=question_id, question_text=question_text, answer=answer
        )
        db.session.add(question)
        db.session.commit()
        return redirect("/questions")


# RETRIEVE LIST OF QUESTIONS
@app.route("/questions")
def RetrieveQuestionsList():
    questions = QuestionModel.query.all()
    return render_template("questionslist.html", questions=questions)


# RETRIEVE SINGLE QUESTION
@app.route("/questions/<int:id>")
def RetrieveSingleQuestion(id):
    question = QuestionModel.query.filter_by(question_id=id).first()
    if question:
        return render_template("questions.html", question=question)
    return f"Question with id = {id} Doesn't exist"


# UPDATE QUESTION
@app.route("/questions/<int:id>/update", methods=["GET", "POST"])
def update(id):
    question = QuestionModel.query.filter_by(question_id=id).first()
    if request.method == "POST":
        if question:
            db.session.delete(question)
            db.session.commit()

            question_text = request.form["question_text"]
            answer = request.form["answer"]
            question = QuestionModel(
                question_id=id, question_text=question_text, answer=answer
            )

            db.session.add(question)
            db.session.commit()
            return redirect(f"/questions/{id}")
        return f"Question with id = {id} Does not exist!"
    return render_template("update.html, question = question")


# DELETE QUESTION
@app.route("/questions/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    question = QuestionModel.query.filter_by(question_id=id).first()
    if request.method == "POST":
        if question:
            db.session.delete(question)
            db.session.commit()
            return redirect("/questions")
        abort(404)
    return render_template("delete.html")


if __name__ == "__main__":

    app.directory = './'
    app.run(host='127.0.0.1', port=5000)

