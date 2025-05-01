from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>User Form</title>
</head>
<body style="font-family: Arial; background-color: #f9f9f9; padding: 20px;">
    <h2>User Information Form</h2>
    <form action="/form" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="age">Age:</label>
        <input type="number" id="age" name="age" required><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

@app.route('/form', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return f'''
        <h1>Thank you!</h1>
        <p>Hello, {name}. Your age is {age}.</p>
        '''
    return render_template_string(form_html)


if __name__ == '__main__':
    app.run(debug=True)
