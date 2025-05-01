from flask import Flask, request, render_template_string

app = Flask(__name__)

# Different HTML structure and message
login_html = '''
<html>
<head>
    <title>User Login</title>
</head>
<body style="background-color: #eef; font-family: Verdana; padding: 40px;">
    <h1 style="color: #333;">Welcome to Secure Login</h1>
    <form action="/login" method="post">
        <p><label>User ID:</label>
        <input type="text" name="user" placeholder="Enter username" required></p>

        <p><label>Secret Key:</label>
        <input type="password" name="pass" placeholder="Enter password" required></p>

        <button type="submit">Sign In</button>
    </form>
</body>
</html>
'''

@app.route('/login', methods=['GET', 'POST'])
def secure_login():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('pass')

        if user == 'admin' and password == '1234':
            return "<h2 style='color: green;'>Access Granted. Welcome, Admin!</h2>"
        else:
            return "<h2 style='color: crimson;'>Access Denied. Please check your credentials.</h2>"

    return render_template_string(login_html)

if __name__ == '__main__':
    app.run(debug=True)
