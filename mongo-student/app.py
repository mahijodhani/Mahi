from flask import Flask, jsonify
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
    try:
        
        students = list(students_collection.find({}, {'_id': 0}))
        return jsonify(students)  # Return the students as a JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
