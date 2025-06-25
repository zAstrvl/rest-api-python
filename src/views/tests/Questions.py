from flask import Blueprint
from src.constants.routes import QUESTION_ROUTE, CHECK_ROUTE, TEST_ROUTE
from controllers import QuestionsController  

question_routes = Blueprint('question_routes', __name__)

# Get parents from db
@question_routes.route(f'/{QUESTION_ROUTE}', methods=['GET']) 
def get_questions_route():
    return QuestionsController.get_questions_controller()
    
# Post parent to db    
@question_routes.route(f'/{QUESTION_ROUTE}', methods=['POST'])
def post_questions_route():
    return QuestionsController.post_question_controller()

# Get question by ID from db
@question_routes.route(f'/{QUESTION_ROUTE}/<int:question_id>', methods=['GET'])
def get_question_route(question_id):
    return QuestionsController.get_question_controller(question_id)

# Put question by ID from db
@question_routes.route(f'/{QUESTION_ROUTE}/<int:question_id>', methods=['PUT'])
def put_question_route(question_id):
    return QuestionsController.put_question_controller(question_id)

# Delete question by ID from db
@question_routes.route(f'/{QUESTION_ROUTE}/<int:question_id>', methods=['DELETE'])
def delete_question_route(question_id):
    return QuestionsController.delete_question_controller(question_id)

@question_routes.route(f'/{QUESTION_ROUTE}/<int:question_id>/{CHECK_ROUTE}', methods=['POST'])
def check_answer(question_id):
    return QuestionsController.check_answer_controller(question_id)

@question_routes.route(f'/{TEST_ROUTE}/{CHECK_ROUTE}', methods=['POST'])
def check_test():
    return QuestionsController.check_test_controller()