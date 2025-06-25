from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os
from functools import wraps
from flask import request, jsonify

def hash_password(password):
    return generate_password_hash(password)

def verify_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

def generate_token(user_id, userType):
    secret = os.environ.get('SECRET_KEY', 'default_secret')
    token = jwt.encode({
        'user_id': user_id,
        'userType': userType,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, secret, algorithm='HS256')
    return token

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(" ")[1]
            if not token:
                return jsonify({'message': 'Token is missing!'}), 401

            secret = os.environ.get('SECRET_KEY', 'default_secret')
            try:
                data = jwt.decode(token, secret, algorithms=['HS256'])
                userType = data.get('userType')
                if userType not in roles:
                    return jsonify({'message': 'You do not have permission for this action!'}), 403
            except Exception:
                return jsonify({'message': 'Token is invalid!'}), 401
            return f(*args, **kwargs)
        return decorated
    return decorator