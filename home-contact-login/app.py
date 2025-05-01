from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Templates for each page
home_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f0f0; margin: 0; padding: 0; }
        .container { width: 70%; margin: auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        h1 { text-align: center; color: #333; }
        .button { padding: 10px 15px; margin: 10px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px; }
        .button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Home Page</h1>
        <a href="{{ url_for('contact') }}" class="button">Go to Contact</a>
        <a href="{{ url_for('login') }}" class="button">Go to Login</a>
    </div>
</body>
</html>
'''

contact_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Contact Page</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f0f0; }
        .container { width: 70%; margin: auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        h1 { text-align: center; color: #333; }
        .button { padding: 10px 15px; margin: 10px; background-color: #007BFF; color: white; text-decoration: none; border-radius: 5px; }
        .button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Contact Us</h1>
        <a href="{{ url_for('home') }}" class="button">Go to Home</a>
        <a href="{{ url_for('login') }}" class="button">Go to Login</a>
    </div>
</body>
</html>
'''

login_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f0f0; }
        .container { width: 70%; margin: auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        h1 { text-align: center; color: #333; }
        .button { padding: 10px 15px; margin: 10px; background-color: #FF9800; color: white; text-decoration: none; border-radius: 5px; }
        .button:hover { background-color: #e68900; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <a href="{{ url_for('home') }}" class="button">Go to Home</a>
        <a href="{{ url_for('contact') }}" class="button">Go to Contact</a>
    </div>
</body>
</html>
'''

# Routes for each page
@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/contact')
def contact():
    return render_template_string(contact_html)

@app.route('/login')
def login():
    return render_template_string(login_html)

if __name__ == '__main__':
    app.run(debug=True)
