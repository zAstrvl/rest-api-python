from flask import jsonify
from models import Parents
from utils import token_required
from src.constants.database import db

@token_required
def post_parent_controller(data):
    name = data.get('name')
    surName = data.get('surName')
    email = data.get('email')
    phone = data.get('phone')

    if not name or not surName or not email or not phone:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    existing_parent = Parents.query.filter_by(email=email).first()
    if existing_parent:
        return jsonify({"success": False, "status code": 409, "message": "Parent already exists"}), 409

    new_parent = Parents(name=name, surName=surName, email=email, phone=phone)
    db.session.add(new_parent)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Parent added successfully"}), 201

@token_required
def get_parents_controller():
    parents = Parents.query.all()
    parent_list = []
    for parent in parents:
        parent_list.append({
            'id': parent.id,
            'name': parent.name,
            'surName': parent.surName,
            'email': parent.email
        })
    return jsonify({"success": True, "status code": 200, "message": "Parent list request successful", "data": {"students": parent_list}}), 200

@token_required
def get_parent_controller(parent_id):
    parent = Parents.query.get(parent_id)
    if not parent:
        return jsonify({"success": False, "status code": 404, "message": "Parent not found"}), 404
    return jsonify({
        'id': parent.id,
        'name': parent.name,
        'surName': parent.surName,
        'email': parent.email
    }), 200

@token_required
def delete_parent_controller(parent_id):
    parent = Parents.query.get(parent_id)
    if not parent:
        return jsonify({"success": False, "status code": 404, "message": "Parent not found"}), 404
    
    db.session.delete(parent)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Parent deleted successfully"}), 200

@token_required
def put_parent_controller(parent_id, data):
    name = data.get('name')
    surName = data.get('surName')
    email = data.get('email')
    phone = data.get('phone')

    parent = Parents.query.get(parent_id)
    if not parent:
        return jsonify({"success": False, "status code": 404, "message": "Parent not found"}), 404

    if not name or not surName or not email or not phone:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    parent.name = name
    parent.surName = surName
    parent.email = email
    parent.phone = phone
    db.session.commit()

    return jsonify({"success": True, "status code": 200, "message": "Parent updated successfully"}), 200