from flask import Blueprint, request
from src.constants.routes import TEACHER_ROUTE
from controllers import TeachersController  

routes = Blueprint('routes', __name__)

# Get parents from db
@routes.route(f'/{TEACHER_ROUTE}', methods=['GET']) 
def get_students_route():
    data = request.get_json()
    return TeachersController.get_teachers_controller(data)
    
# Post parent to db    
@routes.route(f'/{TEACHER_ROUTE}', methods=['POST'])
def post_students_route():
    data = request.get_json()
    return TeachersController.post_teacher_controller(data)

# Get teacher by ID from db
@routes.route(f'/{TEACHER_ROUTE}/<int:teacher_id>', methods=['GET'])
def get_student_route(teacher_id):
    return TeachersController.get_teacher_controller(teacher_id)

# Put teacher by ID from db
@routes.route(f'/{TEACHER_ROUTE}/<int:teacher_id>', methods=['PUT'])
def put_student_route(teacher_id):
    data = request.get_json()
    return TeachersController.put_teacher_controller(teacher_id, data)

# Delete teacher by ID from db
@routes.route(f'/{TEACHER_ROUTE}/<int:teacher_id>', methods=['DELETE'])
def delete_student_route(teacher_id):
    return TeachersController.delete_teacher_controller(teacher_id)