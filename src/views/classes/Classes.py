from flask import Blueprint
from controllers import ClassesController
from utils import role_required
from src.constants.routes import CLASS_ROUTE

class_routes = Blueprint('class_routes', __name__)

@class_routes.route(f'/{CLASS_ROUTE}', methods=['GET'])
def get_classes_route():
    return ClassesController.get_classes_controller()

@class_routes.route(f'/{CLASS_ROUTE}/<int:class_id>', methods=['GET'])
def get_class_route(class_id):
    return ClassesController.get_class_controller(class_id)

@class_routes.route(f'/{CLASS_ROUTE}', methods=['POST'])
def post_class_route():
    return ClassesController.post_class_controller()

@class_routes.route(f'/{CLASS_ROUTE}/<int:class_id>', methods=['PUT'])
def put_class_route(class_id):
    return ClassesController.put_class_controller(class_id)

@class_routes.route(f'/{CLASS_ROUTE}/<int:class_id>', methods=['DELETE'])
def delete_class_route(class_id):
    return ClassesController.delete_class_controller(class_id)

@class_routes.route(f'/{CLASS_ROUTE}/<int:class_id>', methods=['GET'])
def get_class_average_route(class_id):
    return ClassesController.get_class_average_controller(class_id)