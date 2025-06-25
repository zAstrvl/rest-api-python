from flask import jsonify, request
from src.models.classes.Classes import Classes
from src.models.students.Students import Students
from utils import role_required
from src.constants.database import db

from flask import jsonify, request
from src.models.classes.Classes import Classes
from src.models.students.Students import Students
from src.constants.database import db
from utils import role_required

@role_required('TEACHER', 'ADMIN')
def get_classes_controller():
    classes = Classes.query.all()
    class_list = []
    for c in classes:
        class_list.append({
            "id": c.id,
            "averageValue": c.averageValue,
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
    return jsonify({
        "success": True,
        "class": {
            "id": c.id,
            "averageValue": c.averageValue,
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