import os
from flask import (
    Flask,
    request,
    jsonify,
    abort
)
import json
from flask_cors import CORS
import sys

from models import db, setup_db, Teacher, Student
from auth import AuthError, requires_auth
from bson.objectid import ObjectId


def create_app(test_config=None):
    MODELS_PER_PAGE = 10
    #db_drop_and_create_all()
    app = Flask(__name__)
    setup_db(app)
    #migrate = Migrate(app, db)
    CORS(app)

    def paginate_model(request, selection):
        if request:
            page = request.args.get('page', 1, type=int)
        else:
            page = 1
        start = (page-1)*MODELS_PER_PAGE
        end = start + MODELS_PER_PAGE
        models = [m.format() for m in selection]
        current_models = models[start:end]
        return current_models

    @app.route('/teachers', methods=['GET'])
    @requires_auth('get:teachers')
    def get_teachers(jwt):
        teachers = Teacher.query.all()
        current_teachers = paginate_model(request, teachers)
        if len(current_teachers) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'teachers': current_teachers,
            'total_teachers': len(teachers)
        }), 200

    @app.route('/students', methods=['GET'])
    @requires_auth('get:students')
    def get_students(jwt):
        students = Student.query.all()
        print("students----")
        current_students = paginate_model(request, students)
        print("current_students = ", current_students)
        if len(current_students) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'students': current_students,
            'total_students': len(students)
        }), 200
        
    @app.route('/teachers', methods=['POST'])
    @requires_auth('post:teachers')
    def create_teacher(jwt):
        body = request.get_json()
        print("body: ", body)
        name = body.get('name', '')
        try:
            teacher = Teacher(name=name)
            teacher.save()

            selection = Teacher.query.all()
            current_teachers = paginate_model(request, selection)

            return jsonify({
                'success': True,
                'total_teachers': len(selection),
                'teachers': current_teachers
            }), 200
        except Exception as e:
            abort(422)

    @app.route('/students', methods=['POST'])
    @requires_auth('post:students')
    def create_student(jwt):
        body = request.get_json()
        print("body: ", body)
        name = body.get('name', '')
        age = body.get('age', 0)
        gender = body.get('gender', 'M')
        teacher_id = body.get('teacher_id')
        year = body.get('year', 2000)
        try:
            teacher = Teacher.query.get(teacher_id)
            student = Student(name=name, age=int(age), gender=gender, teacher=teacher,year=int(year))
            student.save()
            
            selection = Student.query.all()
            current_students = paginate_model(request, selection)
            print("after current_students")
            return jsonify({
                'success': True,
                'students': current_students,
                'total_students': len(selection)
            }), 200
        except Exception as e:
            abort(422)

    @app.route('/teachers/<teacher_id>', methods=['PATCH'])
    @requires_auth('patch:teachers')
    def update_teacher(jwt, teacher_id):
        body = request.get_json()
        name = body.get('name', None)
        if name is None:
            abort(404)

        try:
            teacher = Teacher.query.get(teacher_id)
            if teacher is None:
                abort(404)
            teacher.name = name
            teacher.save()

            return jsonify({
                'success': True
            }), 200

        except Exception as e:
            abort(422)

    @app.route('/students/<student_id>', methods=['PATCH'])
    @requires_auth('patch:students')
    def update_student(jwt, student_id):
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        year = body.get('year', None)
        try:
            student = Student.query.get(student_id)
            if student is None:
                abort(404)

            student.name = student.name if name is None else name
            student.age = student.age if age is None else age
            student.gender = student.gender if gender is None else gender
            student.year = student.year if year is None else year

            student.save()

            return jsonify({
                'success': True,
                'actor': student.format()
            }), 200
        except Exception as e:
            abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False, 
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
                        'success': False,
                        'error': 404,
                        'message': 'resource not found'
                        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
                        'success': False,
                        'error': 500,
                        'message': 'internal server error'
                        }), 500

    @app.errorhandler(400)
    def bad_error(error):
        return jsonify({
                        'success': False,
                        'error': 400,
                        'message': 'bad request'
                        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
                        'success': False,
                        'error': 405,
                        'message': 'method not allowed'
                        }), 405

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)








