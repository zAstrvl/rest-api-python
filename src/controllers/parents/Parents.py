from flask import jsonify, request
from src.models.parents.Parents import Parents
from src.models.students.Students import Students
from utils import role_required
from src.constants.database import db
from src.constants.usertypes import UserTypes

@role_required('ADMIN')
def post_parent_controller():
    data = request.get_json()
    name = data.get('name')
    surName = data.get('surName')
    email = data.get('email')
    phone = data.get('phone')
    userType = UserTypes.PARENT.name

    if not name or not surName or not email or not phone:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    existing_parent = Parents.query.filter_by(email=email).first()
    if existing_parent:
        return jsonify({"success": False, "status code": 409, "message": "Parent already exists"}), 409
    
    new_parent = Parents(name=name, surName=surName, email=email, phone=phone, userType=userType)
    db.session.add(new_parent)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Parent added successfully"}), 201

@role_required('ADMIN')
def get_parents_controller():
    parents = Parents.query.all()
    parent_list = []
    for parent in parents:
        itsChildren = Students.query.filter_by(parentID=parent.id).all()
        children_list = [
            {
                "id": child.id,
                "name": child.name,
                "surName": child.surName,
                "email": child.email
            }
            for child in itsChildren
        ]
        parent_list.append({
            'id': parent.id,
            'name': parent.name,
            'surName': parent.surName,
            'email': parent.email,
            'phone': parent.phone,
            'itsChildren': children_list
        })
    return jsonify({"success": True, "status code": 200, "message": "Parent list request successful", "data": {"parents": parent_list}}), 200

@role_required('ADMIN')
def get_parent_controller(parent_id):
    parent = Parents.query.get(parent_id)
    if not parent:
        return jsonify({"success": False, "status code": 404, "message": "Parent not found"}), 404
    
    itsChildren = Students.query.filter_by(parentID=parent_id).all()
    children_list = [
        {
            "id": child.id,
            "name": child.name,
            "surName": child.surName,
            "email": child.email
        }
        for child in itsChildren
    ]

    return jsonify({
        "success": True,
        "status code": 200,
        "message": "Parent found",
        "data": {
            'id': parent.id,
            'name': parent.name,
            'surName': parent.surName,
            'email': parent.email,
            'phone': parent.phone,
            'userType': parent.userType.name,
            'itsChildren': children_list
            }
    }), 200

@role_required('ADMIN')
def delete_parent_controller(parent_id):
    parent = Parents.query.get(parent_id)
    if not parent:
        return jsonify({"success": False, "status code": 404, "message": "Parent not found"}), 404
    
    db.session.delete(parent)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Parent deleted successfully"}), 200

@role_required('ADMIN')
def put_parent_controller(parent_id):
    data = request.get_json()
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