from flask import Flask

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process registration form data here
        return "Registration successful!"
    return render_template('register.html')  # Create a register.html template for the registration form

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login form data here
        return "Login successful!"
    return render_template('login.html')  # Create a login.html template for the login form

