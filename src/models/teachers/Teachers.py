from src.constants.database import db

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surName = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    occupation = db.Column(db.String(120), nullable=False)
    started = db.Column(db.Date, nullable=False)
    graduated = db.Column(db.String(120), nullable=False)
    talent = db.Column(db.String(120))
    rate = db.Column(db.Float)

    def __repr__(self):
        return f"<Teacher {self.email}>"