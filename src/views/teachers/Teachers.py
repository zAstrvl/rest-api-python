from flask import Blueprint, request
from src.constants.routes import TEACHER_ROUTE
from controllers import TeachersController  

teacher_routes = Blueprint('teacher_routes', __name__)

# Get parents from db
@teacher_routes.route(f'/{TEACHER_ROUTE}', methods=['GET']) 
def get_teachers_route():
    data = request.get_json()
    return TeachersController.get_teachers_controller()
    
# Post parent to db    
@teacher_routes.route(f'/{TEACHER_ROUTE}', methods=['POST'])
def post_teachers_route():
    data = request.get_json()
    return TeachersController.post_teacher_controller()

# Get teacher by ID from db
@teacher_routes.route(f'/{TEACHER_ROUTE}/<int:teacher_id>', methods=['GET'])
def get_teacher_route(teacher_id):
    return TeachersController.get_teacher_controller(teacher_id)

# Put teacher by ID from db
@teacher_routes.route(f'/{TEACHER_ROUTE}/<int:teacher_id>', methods=['PUT'])
def put_teacher_route(teacher_id):
    data = request.get_json()
    return TeachersController.put_teacher_controller(teacher_id)

# Delete teacher by ID from db
@teacher_routes.route(f'/{TEACHER_ROUTE}/<int:teacher_id>', methods=['DELETE'])
def delete_teacher_route(teacher_id):
    return TeachersController.delete_teacher_controller(teacher_id)