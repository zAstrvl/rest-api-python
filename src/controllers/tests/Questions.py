from flask import jsonify, request
from models import Questions, Answers
from utils import role_required
from src.constants.database import db

@role_required('TEACHER', 'ADMIN')
def post_question_controller():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    answers = data.get('answers')
    type = data.get('type')

    if not title or not answers:
        return jsonify({"success": False, "status code": 400, "message": "No title or answers"}), 400
    
    existing_question = Questions.query.filter_by(title=title).first()
    if existing_question:
        return jsonify({"success": False, "status code": 409, "message": "Question already exists"}), 409
    question = Questions(title=title, description=description, type=type)
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

@role_required('TEACHER', 'ADMIN')
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

@role_required('TEACHER', 'ADMIN')
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

@role_required('TEACHER', 'ADMIN')
def delete_question_controller(question_id):
    question = Questions.query.get(question_id)
    if not question:
        return jsonify({"success": False, "status code": 404, "message": "Question not found"}), 404
    
    db.session.delete(question)
    db.session.commit()
    
    return jsonify({"success": True, "status code": 200, "message": "Question deleted successfully"}), 200

@role_required('TEACHER', 'ADMIN')
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

@role_required('TEACHER', 'ADMIN')
def check_answer_controller(question_id):
    data = request.get_json()
    answer_id = data.get('answer_id')

    question = Questions.query.get(question_id)

    if not question:
        return jsonify({"success": False, "status code": 404,"message": "Question not found"}), 404
    
    answer = Answers.query.filter_by(id=answer_id, question_id=question_id).first()

    if not answer:
        return jsonify({"success": False, "status code": 404, "message": "Answer not found for this question"}), 404
    
    return jsonify({
        "success": True,
        "question": question.title,
        "your_answer": answer.title,
        "isTrue": answer.isTrue,
        "message": "Correct" if answer.isTrue else "Wrong"
    })

@role_required('TEACHER', 'ADMIN', 'STUDENT')
def check_test_controller():
    data = request.get_json()
    answers = data.get('answers', [])
    grade = "F"

    if not answers or not isinstance(answers, list):
        return jsonify({"success": False, "status code": 400, "message": "Answers list required"}), 400

    total = len(answers)
    correct = 0
    details = []

    for item in answers:
        question_id = item.get('question_id')
        answer_id = item.get('answer_id')
        question = Questions.query.get(question_id)
        answer = Answers.query.filter_by(id=answer_id, question_id=question_id).first()
        is_true = answer.isTrue if answer else False
        if is_true:
            correct += 1
        details.append({
            "question_id": question_id,
            "question": question.title if question else None,
            "your_answer": answer.title if answer else None,
            "isTrue": is_true
        })

    average = (correct / total) * 5 if total > 0 else 0
    if average == 5:
        grade = "A"
    elif average < 5 and average >= 4:
        grade = "B"
    elif average < 4 and average >= 3:
        grade = "C"
    elif average < 3 and average >= 2:
        grade = "D"
    elif average < 2 and average >= 1:
        grade = "E"

    return jsonify({
        "success": True,
        "total": total,
        "correct": correct,
        "average": average,
        "details": details,
        "grade": grade
    }), 200