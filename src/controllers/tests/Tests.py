from flask import jsonify
from models import Tests
from utils import token_required
from src.constants.database import db

@token_required
def post_test_controller(data):
    title = data.get('title')
    questions = data.get('questions')

    if not title or not questions:
        return jsonify({"success": False, "status code": 400, "message": "No title or questions"}), 400
    
    existing_test = Tests.query.filter_by(title=title).first()
    if existing_test:
        return jsonify({"success": False, "status code": 409, "message": "Test already exists"}), 409
    
    new_test = Tests(title=title, questions=questions)
    db.session.add(new_test)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Test added successfully"}), 201

@token_required
def get_tests_controller():
    tests = Tests.query.all()
    test_list = []
    for test in tests:
        test_list.append({
            'id': test.id,
            'title': test.title,
            'questions': test.questions
        })
    return jsonify({"success": True, "status code": 200, "message": "Test list request successful", "data": {"students": test_list}}), 200

@token_required
def get_test_controller(test_id):
    test = Tests.query.get(test_id)
    if not test:
        return jsonify({"success": False, "status code": 404, "message": "Test not found"}), 404
    return jsonify({
        'id': test.id,
        'title': test.title,
        'questions': test.questions
    }), 200

@token_required
def delete_test_controller(test_id):
    test = Tests.query.get(test_id)
    if not test:
        return jsonify({"success": False, "status code": 404, "message": "Test not found"}), 404
    
    db.session.delete(test)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Teacher deleted successfully"}), 200

@token_required
def put_test_controller(test_id, data):
    title = data.get('title')
    questions = data.get('questions')

    test = Tests.query.get(test_id)
    if not test:
        return jsonify({"success": False, "status code": 404, "message": "Test not found"}), 404

    if not title or not questions:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    test.title = title
    test.questions = questions
    db.session.add(test)
    db.session.commit()

    return jsonify({"success": True, "status code": 200, "message": "Test updated successfully"}), 200

@token_required
def post_question_controller(data):
    title = data.get('title')
    description = data.get('description')
    isAnswer = data.get('isAnswer')
    answers = data.get('answers')

    if not title or not description or not answers:
        return jsonify({"success": False, "status code": 400, "message": "No title, description or answers"}), 400
    
    existing_test = Tests.query.filter_by(title=title).first()
    if existing_test:
        return jsonify({"success": False, "status code": 409, "message": "Question already exists"}), 409
    
    new_question = Tests(title=title, description=description, answers=answers)
    db.session.add(new_question)
    db.session.commit()

    return jsonify({"success": True, "status code": 201, "message": "Test added successfully"}), 201

@token_required
def get_tests_controller():
    tests = Tests.query.all()
    test_list = []
    for test in tests:
        test_list.append({
            'id': test.id,
            'title': test.title,
            'questions': test.questions
        })
    return jsonify({"success": True, "status code": 200, "message": "Test list request successful", "data": {"students": test_list}}), 200

@token_required
def get_test_controller(test_id):
    test = Tests.query.get(test_id)
    if not test:
        return jsonify({"success": False, "status code": 404, "message": "Test not found"}), 404
    return jsonify({
        'id': test.id,
        'title': test.title,
        'questions': test.questions
    }), 200

@token_required
def delete_test_controller(test_id):
    test = Tests.query.get(test_id)
    if not test:
        return jsonify({"success": False, "status code": 404, "message": "Test not found"}), 404
    
    db.session.delete(test)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Teacher deleted successfully"}), 200

@token_required
def put_test_controller(test_id, data):
    title = data.get('title')
    questions = data.get('questions')

    test = Tests.query.get(test_id)
    if not test:
        return jsonify({"success": False, "status code": 404, "message": "Test not found"}), 404

    if not title or not questions:
        return jsonify({"success": False, "status code": 400, "message": "All fields are required"}), 400

    test.title = title
    test.questions = questions
    db.session.add(test)
    db.session.commit()

    return jsonify({"success": True, "status code": 200, "message": "Test updated successfully"}), 200

