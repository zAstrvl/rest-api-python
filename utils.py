from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime, os
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
            auth_header = request.headers.get('Authorization', None)
            if not auth_header or not auth_header.startswith('Bearer '):
                return jsonify({'message': 'Token is missing!'}), 401

            token = auth_header.split(" ")[1]
            secret = os.environ.get('SECRET_KEY', 'default_secret')
            try:
                data = jwt.decode(token, secret, algorithms=['HS256'])
                user_type = str(data.get('userType', '')).upper()
                allowed_roles = [str(r).upper() for r in roles]
                if user_type not in allowed_roles:
                    return jsonify({'message': 'You do not have permission for this action!'}), 403
            except Exception:
                return jsonify({'message': 'Token is invalid!'}), 401
            return f(*args, **kwargs)
        return decorated
    return decorator