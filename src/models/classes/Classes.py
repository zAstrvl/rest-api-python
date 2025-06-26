from src.constants.database import db
from src.constants.usertypes import UserTypes

class Classes(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    averageValue = db.Column(db.Float)
    students = db.relationship('Students', backref='class', lazy=True, cascade="all, delete-orphan")
    itsTeacher = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
