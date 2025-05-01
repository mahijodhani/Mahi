from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Function to get greeting based on time
def time_based_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# /hello route with query parameter
@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')

    # Validate name (only letters)
    if not name.isalpha():
        return "<h2 style='color:red;'>Invalid name. Please use alphabetic characters only.</h2>"

    greeting = time_based_greeting()
    return f"""
    <html>
        <head>
            <title>Hello Page</title>
        </head>
        <body style="font-family:Arial; background-color:#f0f0f0; text-align:center;">
            <h1>{greeting}, {name}!</h1>
            <p>Welcome to our Flask web application.</p>
            <p>This message is dynamically generated based on the time of your visit.</p>
        </body>
    </html>
    """

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
