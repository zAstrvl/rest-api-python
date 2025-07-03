from flask import Blueprint
from controllers import TestsController
from src.constants.routes import TEST_ROUTE


test_routes = Blueprint('test_routes', __name__)

@test_routes.route(f'/{TEST_ROUTE}', methods=['POST'])
def create_test_route():
    return TestsController.create_test_controller()

@test_routes.route(f'/{TEST_ROUTE}', methods=['GET'])
def get_tests_route():
    return TestsController.get_tests_controller()