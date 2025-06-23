from flask import jsonify, request
from models import Questions
from utils import token_required
from src.constants.database import db

@token_required
def post_question_controller():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({"success": False, "status code": 400, "message": "No title or description"}), 400
    
    existing_question = Questions.query.filter_by(title=title).first()
    if existing_question:
        return jsonify({"success": False, "status code": 409, "message": "Question already exists"}), 409
    
    new_question = Questions(title=title, description=description)
    db.session.add(new_question)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Question added successfully"}), 201

@token_required
def get_questions_controller():
    questions = Questions.query.all()
    question_list = []
    for question in questions:
        question_list.append({
            'id': question.id,
            'title': question.title,
            'description': question.description
        })
    return jsonify({"success": True, "status code": 200, "message": "Question list request successful", "data": {"questions": question_list}}), 200

@token_required
def get_question_controller(question_id):
    question = Questions.query.get(question_id)
    if not question:
        return jsonify({"success": False, "status code": 404, "message": "Question not found"}), 404
    return jsonify({
        "success": True,
        "status code": 200,
        "message": "Question found",
        "data": {
            'id': question.id,
            'title': question.title,
            'description': question.description
        }
    }), 200

@token_required
def delete_question_controller(question_id):
    question = Questions.query.get(question_id)
    if not question:
        return jsonify({"success": False, "status code": 404, "message": "Question not found"}), 404
    
    db.session.delete(question)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Question deleted successfully"}), 200

@token_required
def put_question_controller(question_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    question = Questions.query.get(question_id)
    if not question:
        return jsonify({"success": False, "status code": 404, "message": "Question not found"}), 404

    if not title or not description:
        return jsonify({"success": False, "status code": 400, "message": "Title and description required"}), 400

    question.title = title
    question.description = description
    db.session.add(question)
    db.session.commit()

    return jsonify({"success": True, "status code": 200, "message": "Question updated successfully"}), 200