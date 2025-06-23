from src.controllers.auth import Auth as AuthController
from src.controllers.students import Students as StudentsController
from src.controllers.teachers import Teachers as TeachersController
from src.controllers.parents import Parents as ParentsController
from src.controllers.tests import Questions as QuestionsController
from src.controllers.tests import Answers as AnswersController

__all__ = [
    "AuthController",
    "StudentsController",
    "TeachersController",
    "ParentsController",
    "QuestionsController",
    "AnswersController"
]