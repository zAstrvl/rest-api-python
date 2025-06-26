from src.constants.database import db
from src.constants.usertypes import UserTypes

class Auth(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    confirmPassword = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    surName = db.Column(db.String(120), nullable=False)
    isChecked = db.Column(db.Boolean, default=False)
    userType = db.Column(db.Enum(UserTypes), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"