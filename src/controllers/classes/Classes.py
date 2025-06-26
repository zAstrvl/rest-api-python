from flask import jsonify, request
from src.models.classes.Classes import Classes
from src.models.students.Students import Students
from src.models.teachers.Teachers import Teachers
from utils import role_required
from src.constants.database import db

@role_required('TEACHER', 'ADMIN')
def get_classes_controller():
    classes = Classes.query.all()
    class_list = []
    for c in classes:
        teacher = Teachers.query.get(c.itsTeacher)
        teacher_list = [
            {
                "id": teacher.id,
                "name": teacher.name,
                "surName": teacher.surName,
                "email": teacher.email,
                "occupation": teacher.occupation,
                "started": teacher.started,
                "graduated": teacher.graduated
            } if teacher else None
        ]
        class_list.append({
            "id": c.id,
            "averageValue": c.averageValue,
            "itsTeacher": teacher_list,
            "students": [
                {
                    "id": s.id,
                    "name": s.name,
                    "surName": s.surName,
                    "email": s.email
                } for s in c.students
            ]
        })
    return jsonify({"success": True, "classes": class_list}), 200

@role_required('TEACHER', 'ADMIN')
def get_class_controller(class_id):
    c = Classes.query.get(class_id)
    if not c:
        return jsonify({"success": False, "message": "Class not found"}), 404
    teacher = Teachers.query.get(c.itsTeacher)
    teacher_list = [
            {
                "id": teacher.id,
                "name": teacher.name,
                "surName": teacher.surName,
                "email": teacher.email,
                "occupation": teacher.occupation,
                "started": teacher.started,
                "graduated": teacher.graduated
            } if teacher else None
        ]
    return jsonify({
        "success": True,
        "class": {
            "id": c.id,
            "averageValue": c.averageValue,
            "itsTeacher": teacher_list,
            "students": [
                {
                    "id": s.id,
                    "name": s.name,
                    "surName": s.surName,
                    "email": s.email
                } for s in c.students
            ]
        }
    }), 200

@role_required('TEACHER', 'ADMIN')
def post_class_controller():
    data = request.get_json()
    averageValue = data.get('averageValue')
    itsTeacher = data.get('itsTeacher')
    if itsTeacher is None:
        return jsonify({"success": False, "message": "itsTeacher is required"}), 400
    new_class = Classes(averageValue=averageValue, itsTeacher=itsTeacher)
    db.session.add(new_class)
    db.session.commit()
    return jsonify({"success": True, "message": "Class created", "id": new_class.id}), 201

@role_required('TEACHER', 'ADMIN')
def delete_class_controller(class_id):
    c = Classes.query.get(class_id)
    if not c:
        return jsonify({"success": False, "message": "Class not found"}), 404
    db.session.delete(c)
    db.session.commit()
    return jsonify({"success": True, "message": "Class deleted"}), 200

@role_required('TEACHER', 'ADMIN')
def put_class_controller(class_id):
    c = Classes.query.get(class_id)
    if not c:
        return jsonify({"success": False, "message": "Class not found"}), 404
    data = request.get_json()
    c.averageValue = data.get('averageValue', c.averageValue)
    c.itsTeacher = data.get('itsTeacher', c.itsTeacher)
    db.session.commit()
    return jsonify({"success": True, "message": "Class updated"}), 200

@role_required('TEACHER', 'ADMIN')
def get_class_average_controller(class_id):
    class_obj = Classes.query.get(class_id)
    if not class_obj:
        return jsonify({"success": False, "message": "Class not found"}), 404

    students = Students.query.filter_by(itsClass=class_id).all()
    if not students:
        return jsonify({"success": False, "message": "No students in this class"}), 404
    
    total = sum([s.average for s in students if s.average is not None])
    count = len([s for s in students if s.average is not None])

    average = total / count if count > 0 else 0

    return jsonify({
        "success": True,
        "class_id": class_id,
        "average": average
    }), 200