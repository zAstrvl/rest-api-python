from src.constants.database import db
from src.constants.usertypes import UserTypes

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surName = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    rate = db.Column(db.Float)
    userType = db.Column(db.Enum(UserTypes), nullable=False)
    average = db.Column(db.Float)

    def __repr__(self):
        return f"<Student {self.email}>"