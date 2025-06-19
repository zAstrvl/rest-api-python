from src.models.auth import Auth
from src.models.students import Students
from src.models.teachers import Teachers
from src.models.parents import Parents
from src.constants.database import db


__all__ = ["db", "Auth", "Students", "Teachers", "Parents"]