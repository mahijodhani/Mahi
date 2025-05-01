from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['collegeDB']
students_collection = db['students']

@app.route('/')
def index():
    return "Welcome to the College Database API!"

@app.route('/students', methods=['GET'])
def get_students():
    students = list(students_collection.find({}, {'_id': 0}))
    return {"students": students}

@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        # Display a simple HTML form for adding a student
        return '''
        <h2>Add Student</h2>
        <form method="POST" action="/add-student">
            Name: <input type="text" name="name"><br><br>
            Roll No: <input type="text" name="rollNo"><br><br>
            Department: <input type="text" name="department"><br><br>
            <input type="submit" value="Add Student">
        </form>
        '''
    elif request.method == 'POST':
        name = request.form.get('name')
        roll_no = request.form.get('rollNo')
        department = request.form.get('department')

        if not name or not roll_no or not department:
            return "Missing required fields", 400

        students_collection.insert_one({
            "name": name,
            "rollNo": roll_no,
            "department": department
        })

        return f"Student {name} added successfully!"

if __name__ == '__main__':
    app.run(debug=True)
