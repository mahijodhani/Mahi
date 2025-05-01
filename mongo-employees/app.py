from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  
db = client['company'] 
employees_collection = db['employees']  

@app.route('/')
def index():
    return "Welcome to the Company Database API!"

@app.route('/employees', methods=['GET'])
def get_employees():
    try:
        
        employees = list(employees_collection.find({}, {'_id': 0}))
        return jsonify(employees)  
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
