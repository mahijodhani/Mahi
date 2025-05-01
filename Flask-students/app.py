from flask import Flask, render_template

app = Flask(__name__)

# Route for the /students page
@app.route('/students')
def students():
    student_names = ["Mahi", "Sona", "Riya", "Gunjan", "Palak"]  # List of student names
    return render_template('students.html', students=student_names)

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
