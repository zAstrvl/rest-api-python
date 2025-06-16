from flask import Blueprint, request
from src.constants.routes import AUTH_ROUTE
from controllers import AuthController  

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route(f'/{AUTH_ROUTE}/login', methods=['POST'])
def login_route():
    data = request.get_json()
    # Sadece post_login fonksiyonunu çağırıyoruz
    return AuthController.post_login(data)
    
    
@auth_routes.route(f'/{AUTH_ROUTE}/register', methods=['POST'])
def register_route():
    data = request.get_json()
    # Sadece post_register fonksiyonunu çağırıyoruz
    return AuthController.post_register(data)