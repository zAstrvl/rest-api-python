from flask import Flask
from src.views.auth.Auth import auth_routes
from src.views.students.Students import student_routes
from src.views.parents.Parents import parent_routes
from src.views.teachers.Teachers import teacher_routes
from src.views.tests.Questions import question_routes
from src.constants.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_routes)
app.register_blueprint(student_routes)
app.register_blueprint(parent_routes)
app.register_blueprint(teacher_routes)
app.register_blueprint(question_routes)

if __name__ == '__main__':
    app.run(debug=True)