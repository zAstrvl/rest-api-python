from src.models.auth.Auth import Auth
from src.models.students.Students import Students
from src.models.teachers.Teachers import Teachers
from src.models.parents.Parents import Parents
from src.models.tests.Questions import Questions
from src.models.tests.Answers import Answers
from src.constants.database import db


__all__ = ["db", "Auth", "Students", "Teachers", "Parents", "Questions", "Answers"]