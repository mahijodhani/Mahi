from flask import Flask

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return '''
    <h1>Welcome to Our Website</h1>
    <p>This is the homepage of our awesome Flask web app.</p>
    '''

# About route
@app.route('/about')
def about():
    return '''
    <h1>About Us</h1>
    <p>I am Mahi Jodhani and  this is my  first web app built for my practical exam.</p>
    '''

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
