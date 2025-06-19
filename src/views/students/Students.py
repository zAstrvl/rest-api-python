from flask import Blueprint, request
from controllers import StudentsController 
from src.constants.routes import STUDENT_ROUTE

routes = Blueprint('routes', __name__)

# Get students from db
@routes.route(f'/{STUDENT_ROUTE}', methods=['GET']) 
def get_students_route():
    data = request.get_json()
    return StudentsController.get_students_controller(data)
    
# Post students to db    
@routes.route(f'/{STUDENT_ROUTE}', methods=['POST'])
def post_students_route():
    data = request.get_json()
    return StudentsController.post_student_controller(data)

# Get student by ID from db
@routes.route(f'/{STUDENT_ROUTE}/<int:student_id>', methods=['GET'])
def get_student_route(student_id):
    return StudentsController.get_student_controller(student_id)

# Put student by ID from db
@routes.route(f'/{STUDENT_ROUTE}/<int:student_id>', methods=['PUT'])
def put_student_route(student_id):
    data = request.get_json()
    return StudentsController.put_student_controller(student_id, data)

# Delete student by ID from db
@routes.route(f'/{STUDENT_ROUTE}/<int:student_id>', methods=['DELETE'])
def delete_student_route(student_id):
    return StudentsController.delete_student_controller(student_id)