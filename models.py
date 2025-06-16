from instance import database as db
from src.models.auth import Auth
from src.models.students import Students
from src.models.teachers import Teachers
from src.models.parents import Parents


__all__ = ["db", "Auth", "Students", "Teachers", "Parents"]