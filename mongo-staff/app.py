from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['collegeDB']
staff_collection = db['staff']

@app.route('/')
def index():
    return "Welcome to the College Staff API!"

@app.route('/staff', methods=['GET'])
def get_staff():
    try:
        staff = list(staff_collection.find({}, {'_id': 0}))  # Exclude _id for cleaner output
        return jsonify(staff)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
