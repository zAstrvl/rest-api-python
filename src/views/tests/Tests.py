from flask import Blueprint, request
from src.constants.routes import TEST_ROUTE
from controllers import TestsController

tests_routes = Blueprint('tests_routes', __name__)

# Get parents from db
@tests_routes.route(f'/{TEST_ROUTE}', methods=['GET']) 
def get_tests_route():
    data = request.get_json()
    return TestsController.get_tests_controller(data)
    
# Post parent to db    
@tests_routes.route(f'/{TEST_ROUTE}', methods=['POST'])
def post_tests_route():
    data = request.get_json()
    return TestsController.post_test_controller(data)

# Get test by ID from db
@tests_routes.route(f'/{TEST_ROUTE}/<int:test_id>', methods=['GET'])
def get_test_route(test_id):
    return TestsController.get_test_controller(test_id)

# Put test by ID from db
@tests_routes.route(f'/{TEST_ROUTE}/<int:test_id>', methods=['PUT'])
def put_test_route(test_id):
    data = request.get_json()
    return TestsController.put_test_controller(test_id, data)

# Delete test by ID from db
@tests_routes.route(f'/{TEST_ROUTE}/<int:test_id>', methods=['DELETE'])
def delete_test_route(test_id):
    return TestsController.delete_test_controller(test_id)