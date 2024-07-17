from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the calculator
html_template = '''
<!doctype html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form method="post">
        <input type="text" name="num1" placeholder="Enter first number">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="text" name="num2" placeholder="Enter second number">
        <input type="submit" value="Calculate">
    </form>
    {% if result is not none %}
    <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2
        except (ValueError, ZeroDivisionError):
            result = "Error"

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
