from flask import Blueprint, request
from src.constants.routes import PARENT_ROUTE
from controllers import ParentsController  

parent_routes = Blueprint('parent_routes', __name__)

# Get parents from db
@parent_routes.route(f'/{PARENT_ROUTE}', methods=['GET']) 
def get_parents_route():
    data = request.get_json()
    return ParentsController.get_parents_controller(data)
    
# Post parent to db    
@parent_routes.route(f'/{PARENT_ROUTE}', methods=['POST'])
def post_parents_route():
    data = request.get_json()
    return ParentsController.post_parent_controller(data)

# Get parent by ID from db
@parent_routes.route(f'/{PARENT_ROUTE}/<int:parent_id>', methods=['GET'])
def get_parent_route(parent_id):
    return ParentsController.get_parent_controller(parent_id)

# Put parent by ID from db
@parent_routes.route(f'/{PARENT_ROUTE}/<int:parent_id>', methods=['PUT'])
def put_parent_route(parent_id):
    data = request.get_json()
    return ParentsController.put_parent_controller(parent_id, data)

# Delete parent by ID from db
@parent_routes.route(f'/{PARENT_ROUTE}/<int:parent_id>', methods=['DELETE'])
def delete_parent_route(parent_id):
    return ParentsController.delete_parent_controller(parent_id)