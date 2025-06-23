from src.models.auth.Auth import Auth
from src.models.students.Students import Students
from src.models.teachers.Teachers import Teachers
from src.models.parents.Parents import Parents
from src.models.tests.Tests import Tests
from src.constants.database import db


__all__ = ["db", "Auth", "Students", "Teachers", "Parents", "Tests"]