from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class QuestionModel(db.Model):
    __tablename__ = "question_table"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer(), unique=True)
    question_label = db.Column(db.String())
    question_text = db.Column(db.String())
    answer = db.Column(db.String())

    def __init__(self, question_id, question_label, question_text, answer):
        self.question_id = question_id
        self.question_label = question_label
        self.question_text = question_text
        self.answer = answer

    def __repr__(self):
        return f"{self.question_text}:{self.question_id}"


class AnswerModel(db.Model):
    __tablename__ = "answer_table"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer())
    candidate_id = db.Column(db.Integer())
    question_label = db.Column(db.String())
    answer = db.Column(db.String())
    correct = db.Column(db.Boolean())

    def __init__(self, question_id, candidate_id, question_label, answer, correct):
        self.question_id = question_id
        self.candidate_id = candidate_id
        self.question_label = question_label
        self.answer = answer
        self.correct = correct

    def __repr__(self):
        return f"{self.answer}:{self.question_id}"


# class CandidateModel(db.Model):
#     __tablename__ = "table"

#     id = db.Column(db.Integer, primary_key=True)
#     question_id = db.Column(db.Integer(), unique=True)
#     question_text = db.Column(db.String())
#     answer = db.Column(db.String())

#     def __init__(self, question_id, question_text, answer):
#         self.question_id = question_id
#         self.question_text = question_text
#         self.answer = answer

#     def __repr__(self):
#         return f"{self.question_text}:{self.question_id}"
