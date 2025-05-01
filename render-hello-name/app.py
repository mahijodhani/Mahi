from flask import Flask, render_template

app = Flask(__name__)

# Route with a dynamic URL parameter (name)
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
