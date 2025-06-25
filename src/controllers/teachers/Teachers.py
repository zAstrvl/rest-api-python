from flask import jsonify, request
from src.models.teachers.Teachers import Teachers
from utils import role_required
from src.constants.database import db
from src.constants.usertypes import UserTypes
from datetime import datetime

@role_required('ADMIN')
def post_teacher_controller():
    data = request.get_json()
    name = data.get('name')
    surName = data.get('surName')
    email = data.get('email')
    occupation = data.get('occupation')
    started_str = data.get('started')
    graduated_str = data.get('graduated')
    userType = UserTypes.TEACHER.name

    started = datetime.strptime(started_str, "%d/%m/%Y").date() if started_str else None
    graduated = datetime.strptime(graduated_str, "%d/%m/%Y").date() if graduated_str else None

    if not name or not surName or not email or not occupation or not started or not graduated:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    existing_teacher = Teachers.query.filter_by(email=email).first()
    if existing_teacher:
        return jsonify({"success": False, "status code": 409, "message": "Teacher already exists"}), 409

    new_teacher = Teachers(name=name, surName=surName, email=email, occupation=occupation, started=started, graduated=graduated, userType=userType)
    db.session.add(new_teacher)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Teacher added successfully"}), 201

@role_required('ADMIN')
def get_teachers_controller():
    teachers = Teachers.query.all()
    teacher_list = []
    for teacher in teachers:
        teacher_list.append({
            'id': teacher.id,
            'name': teacher.name,
            'surName': teacher.surName,
            'email': teacher.email,
            'occupation': teacher.occupation,
            'started': teacher.started,
            'graduated': teacher.graduated
        })
    return jsonify({"success": True, "status code": 200, "message": "Teacher list request successful", "data": {"teachers": teacher_list}}), 200

@role_required('ADMIN')
def get_teacher_controller(teacher_id):
    teacher = Teachers.query.get(teacher_id)
    if not teacher:
        return jsonify({"success": False, "status code": 404, "message": "Teacher not found"}), 404
    return jsonify({
        "success": True,
        "status code": 200,
        "message": "Teacher found",
        "data": {
            'id': teacher.id,
            'name': teacher.name,
            'surName': teacher.surName,
            'email': teacher.email,
            'occupation': teacher.occupation,
            'started': teacher.started,
            'graduated': teacher.graduated
        }
    }), 200

@role_required('ADMIN')
def delete_teacher_controller(teacher_id):
    teacher = Teachers.query.get(teacher_id)
    if not teacher:
        return jsonify({"success": False, "status code": 404, "message": "Teacher not found"}), 404
    
    db.session.delete(teacher)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Teacher deleted successfully"}), 200

@role_required('ADMIN')
def put_teacher_controller(teacher_id):
    data = request.get_json()
    name = data.get('name')
    surName = data.get('surName')
    email = data.get('email')
    occupation = data.get('occupation')
    started_str = data.get('started')
    graduated_str = data.get('graduated')

    started = datetime.strptime(started_str, "%d/%m/%Y").date() if started_str else None
    graduated = datetime.strptime(graduated_str, "%d/%m/%Y").date() if graduated_str else None

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