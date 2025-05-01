from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['companyDB']
employees_collection = db['employees']

@app.route('/')
def index():
    return "Welcome to the Company Database API!"

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = list(employees_collection.find({}, {'_id': 0}))
    return {"employees": employees}

@app.route('/add-employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'GET':
        # Display a simple HTML form for adding an employee
        return '''
        <h2>Add Employee</h2>
        <form method="POST" action="/add-employee">
            Name: <input type="text" name="name"><br><br>
            Employee No: <input type="text" name="empNo"><br><br>
            Expertise: <input type="text" name="expertise"><br><br>
            <input type="submit" value="Add Employee">
        </form>
        '''
    elif request.method == 'POST':
        name = request.form.get('name')
        emp_no = request.form.get('empNo')
        expertise = request.form.get('expertise')

        if not name or not emp_no or not expertise:
            return "Missing required fields", 400

        employees_collection.insert_one({
            "name": name,
            "empNo": emp_no,
            "expertise": expertise
        })

        return f"Employee {name} added successfully!"

if __name__ == '__main__':
    app.run(debug=True)
