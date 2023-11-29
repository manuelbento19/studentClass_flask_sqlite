from flask import Blueprint,request
import json
from database import db
from entities.Student import Student

connection = db.createConnection()
database = connection.cursor()

student_router = Blueprint("student",__name__)

def StudentMapper(student):
    return {
        "id": student[0],
        "firstName": student[1],
        "lastName": student[2],
        "course": student[3]
    }


@student_router.route('/',methods=["GET"])
def getStudents():
    database.execute('select * from students')
    results = database.fetchall()
    students = []
    for student in results:
        students.append(StudentMapper(student))
    return students

@student_router.route('/',methods=["POST"])
def createStudent():
    body = request.get_json()
    student = Student(body["firstName"],body["lastName"],body["course"])
    database.execute('insert into students values(?,?,?,?)',(student.id,student.firstName,student.lastName,student.course))
    connection.commit()    
    return {
        "message": "Student created"
    }, 201

@student_router.route('/<student_id>')
def getStudentById(student_id):
    database.execute('select * from students where id=?',(student_id,))
    student = database.fetchone()
    return StudentMapper(student)

@student_router.route('/<student_id>', methods=['PUT'])
def update_student(student_id):
    body = request.get_json()
    student = Student(body["firstName"],body["lastName"],body["course"])
    database.execute("update students set firstName = ?, lastName = ?, course = ? where id=?",(student.firstName, student.lastName, student.course, student_id))
    connection.commit()
    return {
        "message": "Student updated"
    }

@student_router.route('/<student_id>', methods=['DELET'])
def delete_student(student_id):
    database.execute("delete from students where id=?",(student_id,))
    connection.commit()
    return {
        "message": "Student deleted"
    }