from flask_mongoalchemy import MongoAlchemy
import datetime

DB_NAME = 'minedudb'

db = MongoAlchemy()

def setup_db(app, database_name=DB_NAME):
    app.config['MONGOALCHEMY_SERVER'] = "localhost"
    app.config['MONGOALCHEMY_PORT'] = 27017
    app.config['MONGOALCHEMY_USER'] = None
    app.config['MONGOALCHEMY_PASSWORD'] = None
    app.config['MONGOALCHEMY_DATABASE'] = DB_NAME

    db.app = app
    db.init_app(app)

class Teacher(db.Document):
    name = db.StringField()

    def format(self):
        return {
            'name': self.name
        }

class Student(db.Document):
    name = db.StringField()
    age = db.IntField()
    gender = db.StringField()
    teacher = db.DocumentField(Teacher)
    year = db.IntField()

    def format(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'teacher': self.teacher.name,
            'year': self.year
        }


