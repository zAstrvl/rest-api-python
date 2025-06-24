from flask import jsonify, request
from models import Questions, Answers
from utils import token_required
from src.constants.database import db

@token_required
def post_question_controller():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    answers = data.get('answers')

    if not title or not answers:
        return jsonify({"success": False, "status code": 400, "message": "No title or answers"}), 400
    
    existing_question = Questions.query.filter_by(title=title).first()
    if existing_question:
        return jsonify({"success": False, "status code": 409, "message": "Question already exists"}), 409
    question = Questions(title=title, description=description)
    db.session.add(question)
    db.session.commit()

    for ans in answers:
        answer = Answers(
            title=ans.get('title'),
            isTrue=ans.get('isTrue', False),
            question_id=question.id
                         )
        db.session.add(answer)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Question and answers added successfully"}), 201

@token_required
def get_questions_controller():
    questions = Questions.query.all()
    question_list = []
    for question in questions:
        question_list.append({
            'id': question.id,
            'title': question.title,
            'description': question.description,
            'answers': [
                {
                    'id': answer.id,
                    'title': answer.title,
                    'isTrue': answer.isTrue
                }
                for answer in question.answers
            ]
        })
    return jsonify({"success": True, "status code": 200, "message": "Question list request successful", "data": {"questions": question_list}}), 200

@token_required
def get_question_controller(question_id):
    question = Questions.query.get(question_id)
    if not question:
        return jsonify({"success": False, "status code": 404,"message": "Question not found"}), 404

    answers = [
        {"id": a.id, "title": a.title, "isTrue": a.isTrue}
        for a in question.answers
    ]

    return jsonify({
        "success": True,
        "status code": 200,
        "message": "Question found",
        "data": {
            "id": question.id,
            "title": question.title,
            "description": question.description,
            "answers": answers
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
    answers = data.get('answers')

    question = Questions.query.get(question_id)
    if not question:
        return jsonify({"success": False, "status code": 404, "message": "Question not found"}), 404

    if not title or not answers:
        return jsonify({"success": False, "status code": 400, "message": "Title and answers data required"}), 400
    
    for answer in question.answers:
        db.session.delete(answer)
    db.session.commit()

    for ans in answers:
        new_answer = Answers(
            title=ans.get('title'),
            isTrue=ans.get('isTrue', False),
            question_id=question.id
        )
        db.session.add(new_answer)
    
    question.title = title
    question.description = description
    
    db.session.commit()

    return jsonify({"success": True, "status code": 200, "message": "Question updated successfully"}), 200