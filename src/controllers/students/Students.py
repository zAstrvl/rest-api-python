from flask import jsonify, request
from src.models.students.Students import Students
from utils import role_required
from src.constants.database import db
from src.constants.usertypes import UserTypes

@role_required('ADMIN')
def post_student_controller():
    data = request.get_json()
    name = data.get('name')
    surName = data.get('surName')
    email = data.get('email')
    userType = UserTypes.STUDENT

    if not name or not surName or not email:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    existing_student = Students.query.filter_by(email=email).first()
    if existing_student:
        return jsonify({"success": False, "status code": 409, "message": "Student already exists"}), 409

    new_student = Students(name=name, surName=surName, email=email, userType=userType)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Student added successfully"}), 201

@role_required('ADMIN')
def get_students_controller():
    students = Students.query.all()
    student_list = []
    for student in students:
        student_list.append({
            'id': student.id,
            'name': student.name,
            'surName': student.surName,
            'email': student.email,
            'userType': student.userType.name
        })
    return jsonify({"success": True, "status code": 200, "message": "Student list request successful", "data": {"students": student_list}}), 200

@role_required('ADMIN')
def get_student_controller(student_id):
    student = Students.query.get(student_id)
    if not student:
        return jsonify({"success": False, "status code": 404, "message": "Student not found"}), 404
    return jsonify({
        "success": True,
        "status code": 200,
        "message": "Student found",
        "data": {
            'id': student.id,
            'name': student.name,
            'surName': student.surName,
            'email': student.email,
            'userType': student.userType.name
            }
        }), 200

@role_required('ADMIN')
def delete_student_controller(student_id):
    student = Students.query.get(student_id)
    if not student:
        return jsonify({"success": False, "status code": 404, "message": "Student not found"}), 404
    
    db.session.delete(student)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Student deleted successfully"}), 200

@role_required('ADMIN')
def put_student_controller(student_id):
    data = request.get_json()
    name = data.get('name')
    surName = data.get('surName')
    email = data.get('email')

    student = Students.query.get(student_id)
    if not student:
        return jsonify({"success": False, "status code": 404, "message": "Student not found"}), 404

    if not name or not surName or not email:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    student.name = name
    student.surName = surName
    student.email = email
    db.session.commit()

    return jsonify({"success": True, "status code": 200, "message": "Student updated successfully"}), 200