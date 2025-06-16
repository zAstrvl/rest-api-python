from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    confirmPassword = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    surName = db.Column(db.String(120), nullable=False)
    isChecked = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Auth {self.email}>"