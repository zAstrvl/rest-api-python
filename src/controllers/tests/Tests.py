from flask import jsonify, request
from src.models.tests.Tests import Tests, TestQuestions
from src.models.tests.Questions import Questions
from src.constants.database import db
from utils import role_required

@role_required('TEACHER', 'ADMIN')
def create_test_controller():
    data = request.get_json()
    title = data.get('title')
    question_ids = data.get('question_ids', [])

    if not title or not question_ids or not isinstance(question_ids, list):
        return jsonify({"success": False, "message": "Title and question_ids required"}), 400

    new_test = Tests(title=title)
    db.session.add(new_test)
    db.session.flush()  # new_test.id almak için

    for qid in question_ids:
        if Questions.query.get(qid):
            tq = TestQuestions(test_id=new_test.id, question_id=qid)
            db.session.add(tq)

    db.session.commit()
    return jsonify({"success": True, "message": "Test created", "test_id": new_test.id}), 201

@role_required('TEACHER', 'ADMIN')
def get_tests_controller():
    tests = Tests.query.all()
    test_list = []
    for t in tests:
        test_list.append({
            "id": t.id,
            "title": t.title,
            "questions": [tq.question_id for tq in t.questions]
        })
    return jsonify({"success": True, "tests": test_list}), 200