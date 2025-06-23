from src.constants.database import db

class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    isTrue = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Answer {self.id}>"