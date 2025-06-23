from src.constants.database import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    isAnswer = db.Column(db.Boolean, nullable=False)
    answers = db.relationship('Answers', backref='question', lazy=True)
    testID = db.Column(db.Integer, db.ForeignKey('tests.id'), nullable=False)

    def __repr__(self):
        return f"<Question {self.id}>"