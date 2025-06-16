from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Parents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surName = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Parent {self.email}>"