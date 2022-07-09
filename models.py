from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class QuestionModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer(), unique=True)
    question_text = db.Column(db.String())
    answer = db.Column(db.String())

    def __init__(self, question_id, question_text, answer):
        self.question_id = question_id
        self.question_text = question_text
        self.answer = answer

    def __repr__(self):
        return f"{self.question_text}:{self.question_id}"
