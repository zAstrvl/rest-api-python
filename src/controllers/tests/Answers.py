from flask import jsonify, request
from models import Answers
from utils import token_required
from src.constants.database import db

@token_required
def post_answer_controller():
    data = request.get_json()
    title = data.get('title')
    answer_id = data.get('answer_id')

    if not title or not answer_id:
        return jsonify({"success": False, "status code": 400, "message": "No title or answer ID"}), 400
    
    existing_answer = Answers.query.filter_by(title=title).first()
    if existing_answer:
        return jsonify({"success": False, "status code": 409, "message": "Answer already exists"}), 409
    
    new_answer = Answers(title=title, answer_id=answer_id)
    db.session.add(new_answer)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Answer added successfully"}), 201

@token_required
def get_answers_controller():
    answers = Answers.query.all()
    answer_list = []
    for answer in answers:
        answer_list.append({
            'id': answer.id,
            'title': answer.title,
            'question_id': answer.question_id
        })
    return jsonify({"success": True, "status code": 200, "message": "Answer list request successful", "data": {"students": answer_list}}), 200

@token_required
def get_answer_controller(answer_id):
    answer = Answers.query.get(answer_id)
    if not answer:
        return jsonify({"success": False, "status code": 404, "message": "Answer not found"}), 404
    return jsonify({
        'id': answer.id,
        'title': answer.title,
        'description': answer.question_id
    }), 200

@token_required
def delete_answer_controller(answer_id):
    answer = Answers.query.get(answer_id)
    if not answer:
        return jsonify({"success": False, "status code": 404, "message": "Answer not found"}), 404
    
    db.session.delete(answer)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Answer deleted successfully"}), 200

@token_required
def put_answer_controller(answer_id):
    data = request.get_json()
    title = data.get('title')
    question_id = data.get('question_id')

    answer = Answers.query.get(answer_id)
    if not answer:
        return jsonify({"success": False, "status code": 404, "message": "Answer not found"}), 404

    if not title or not question_id:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    answer.title = title
    answer.question_id = question_id
    db.session.add(answer)
    db.session.commit()

    return jsonify({"success": True, "status code": 200, "message": "Answer updated successfully"}), 200