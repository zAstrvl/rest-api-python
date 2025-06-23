from flask import Blueprint
from controllers import StudentsController 
from src.constants.routes import STUDENT_ROUTE

student_routes = Blueprint('student_routes', __name__)

# Get students from db
@student_routes.route(f'/{STUDENT_ROUTE}', methods=['GET']) 
def get_students_route():
    return StudentsController.get_students_controller()
    
# Post students to db    
@student_routes.route(f'/{STUDENT_ROUTE}', methods=['POST'])
def post_students_route():
    return StudentsController.post_student_controller()

# Get student by ID from db
@student_routes.route(f'/{STUDENT_ROUTE}/<int:student_id>', methods=['GET'])
def get_student_route(student_id):
    return StudentsController.get_student_controller(student_id)

# Put student by ID from db
@student_routes.route(f'/{STUDENT_ROUTE}/<int:student_id>', methods=['PUT'])
def put_student_route(student_id):
    return StudentsController.put_student_controller(student_id)

# Delete student by ID from db
@student_routes.route(f'/{STUDENT_ROUTE}/<int:student_id>', methods=['DELETE'])
def delete_student_route(student_id):
    return StudentsController.delete_student_controller(student_id)