from flask import Blueprint, request
from src.constants.routes import ANSWER_ROUTE
from controllers import AnswersController  

answer_routes = Blueprint('answers_route', __name__)

# Get parents from db
@answer_routes.route(f'/{ANSWER_ROUTE}', methods=['GET']) 
def get_answers_route():
    return AnswersController.get_answers_controller()
    
# Post parent to db    
@answer_routes.route(f'/{ANSWER_ROUTE}', methods=['POST'])
def post_answers_route():
    return AnswersController.post_answer_controller()

# Get answer by ID from db
@answer_routes.route(f'/{ANSWER_ROUTE}/<int:answer_id>', methods=['GET'])
def get_answer_route(answer_id):
    return AnswersController.get_answer_controller(answer_id)

# Put answer by ID from db
@answer_routes.route(f'/{ANSWER_ROUTE}/<int:answer_id>', methods=['PUT'])
def put_answer_route(answer_id):
    return AnswersController.put_answer_controller(answer_id)

# Delete answer by ID from db
@answer_routes.route(f'/{ANSWER_ROUTE}/<int:answer_id>', methods=['DELETE'])
def delete_answer_route(answer_id):
    return AnswersController.delete_answer_controller(answer_id)