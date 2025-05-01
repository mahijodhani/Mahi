from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the /feedback page
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    name = ""
    feedback = ""
    if request.method == 'POST':
        
        name = request.form.get('name')
        feedback = request.form.get('feedback')
    return render_template('feedback.html', name=name, feedback=feedback)


if __name__ == '__main__':
    app.run(debug=True)
