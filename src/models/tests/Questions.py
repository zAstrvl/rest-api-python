from src.constants.database import db
from src.constants.usertypes import UserTypes

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    answers = db.relationship('Answers', backref='question', lazy=True, cascade="all, delete-orphan")
    type = db.Column(db.Enum(UserTypes), nullable=False)
    average = db.Column(db.Float)
    
    def __repr__(self):
        return f"<Question {self.id}>"