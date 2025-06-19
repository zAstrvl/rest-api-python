from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.views.auth.Auth import auth_routes
from src.constants.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Blueprint'leri ekleyin
app.register_blueprint(auth_routes)

if __name__ == '__main__':
    app.run(debug=True)