from flask import jsonify
from models import Teachers
from utils import token_required
from src.constants.database import db

@token_required
def post_teacher_controller(data):
    name = data.get('name')
    surName = data.get('surName')
    email = data.get('email')
    occupation = data.get('occupation')
    started = data.get('started')
    graduated = data.get('graduated')

    if not name or not surName or not email or not occupation or not started or not graduated:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    existing_teacher = Teachers.query.filter_by(email=email).first()
    if existing_teacher:
        return jsonify({"success": False, "status code": 409, "message": "Teacher already exists"}), 409

    new_teacher = Teachers(name=name, surName=surName, email=email, occupation=occupation, started=started, graduated=graduated)
    db.session.add(new_teacher)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Teacher added successfully"}), 201

@token_required
def get_teachers_controller():
    teachers = Teachers.query.all()
    teacher_list = []
    for teacher in teachers:
        teacher_list.append({
            'id': teacher.id,
            'name': teacher.name,
            'surName': teacher.surName,
            'email': teacher.email
        })
    return jsonify({"success": True, "status code": 200, "message": "Teacher list request successful", "data": {"students": teacher_list}}), 200

@token_required
def get_teacher_controller(teacher_id):
    teacher = Teachers.query.get(teacher_id)
    if not teacher:
        return jsonify({"success": False, "status code": 404, "message": "Teacher not found"}), 404
    return jsonify({
        'id': teacher.id,
        'name': teacher.name,
        'surName': teacher.surName,
        'email': teacher.email
    }), 200

@token_required
def delete_teacher_controller(teacher_id):
    teacher = Teachers.query.get(teacher_id)
    if not teacher:
        return jsonify({"success": False, "status code": 404, "message": "Teacher not found"}), 404
    
    db.session.delete(teacher)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Teacher deleted successfully"}), 200

@token_required
def put_teacher_controller(teacher_id, data):
    name = data.get('name')
    surName = data.get('surName')
    email = data.get('email')
    occupation = data.get('occupation')
    started = data.get('started')
    graduated = data.get('graduated')

    teacher = Teachers.query.get(teacher_id)
    if not teacher:
        return jsonify({"success": False, "status code": 404, "message": "Teacher not found"}), 404

    if not name or not surName or not email or not occupation or not started or not graduated:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    teacher.name = name
    teacher.surName = surName
    teacher.email = email
    teacher.occupation = occupation
    teacher.started = started
    teacher.graduated = graduated
    db.session.commit()

    return jsonify({"success": True, "status code": 200, "message": "Teacher updated successfully"}), 200