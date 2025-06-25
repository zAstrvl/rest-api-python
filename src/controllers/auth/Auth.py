from flask import jsonify
from src.models.auth.Auth import Auth
from werkzeug.security import check_password_hash, generate_password_hash
from utils import generate_token
from src.constants.database import db
from src.constants.usertypes import UserTypes

def login(email, password):
    user = Auth.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return generate_token(user.id, user.userType.name)
    return None

def post_login(data):
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"success": False, "status code": 400, "message": "Email and password are required"}), 400
    
    token = login(email, password)
    
    if token:
        return jsonify({"success": True, "status code": 200, "message": "Token is valid", "data": {"token": token}}), 200
    else:
        return jsonify({"success": False, "status code": 401, "message": "Invalid credentials"}), 401
    
def post_register(data):
    email = data.get('email')
    password = data.get('password')
    confirmPassword = data.get('confirmPassword')
    name = data.get('name')
    surName = data.get('surName')
    isChecked = data.get('isChecked')
    userType = data.get('userType')

    existing_email = Auth.query.filter_by(email=email).first()
    
    if not email or not password or not confirmPassword or not name or not surName:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400
    
    if password != confirmPassword:
        return jsonify({"success": False, "status code": 400, "message": "Passwords do not match"}), 400
    if isChecked is False:
        return jsonify({"success": False, "status code": 400, "message": "You must agree to the terms"}), 400
    if existing_email:
        return jsonify({"success": False, "status code": 409, "message": "Admin already exists"}), 409
    
    hashedPassword = generate_password_hash(password)
    new_admin = Auth(email=email, password=hashedPassword, confirmPassword=hashedPassword, name=name, surName=surName, isChecked=isChecked, userType=userType)
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({"success": True, "status code": 201, "message": "Admin registered successfully"}), 201
    