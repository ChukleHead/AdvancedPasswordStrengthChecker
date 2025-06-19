from flask import Flask, render_template, request
import re
import math

app = Flask(__name__)

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[^A-Za-z0-9]', password): charset += 32
    entropy = len(password) * math.log2(charset) if charset > 0 else 0
    return round(entropy, 2)

def get_feedback(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Use at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Add uppercase letters.")
    if not re.search(r'[a-z]', password):
        feedback.append("Include lowercase letters.")
    if not re.search(r'\d', password):
        feedback.append("Include numbers.")
    if not re.search(r'[^A-Za-z0-9]', password):
        feedback.append("Add special characters.")
    if password.lower() in ['password', '123456', 'qwerty', 'admin']:
        feedback.append("Avoid common passwords.")
    return " ".join(feedback) if feedback else "Great password!"

def evaluate_password(password):
    entropy = calculate_entropy(password)
    if entropy > 80:
        strength = "Very Strong"
    elif entropy > 60:
        strength = "Strong"
    elif entropy > 40:
        strength = "Moderate"
    else:
        strength = "Weak"
    return strength, get_feedback(password)

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    feedback = None
    if request.method == 'POST':
        password = request.form['password']
        strength, feedback = evaluate_password(password)
    return render_template('index.html', strength=strength, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
