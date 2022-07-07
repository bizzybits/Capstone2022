from os import abort
from flask import Flask, render_template, request, redirect
from models import db, QuestionModel

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quizgame.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route("/")
def index():
    greetings = "Hello World"
    return render_template("home.html", greetings=greetings)


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
    app.directory = "./"
    app.run(host="127.0.0.1", port=5000)
