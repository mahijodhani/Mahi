from flask import Flask, render_template

app = Flask(__name__)

# Route for /marks/<int:score>
@app.route('/marks/<int:score>')
def marks(score):
    return render_template('marks.html', score=score)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
