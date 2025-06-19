# Advanced Password Strength Checker

This is an advanced web-based password strength checker built using Flask. It evaluates passwords using:
- Entropy-based strength scoring
- Checks for uppercase, lowercase, numbers, and symbols
- Detects weak/common passwords
- Provides real-time feedback for improvements

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run app: `python app.py`
3. Open in browser: `http://127.0.0.1:5000`

## Tip
If getting a "ImportError: cannot import name 'url_quote' from 'werkzeug.urls'" error use command : `pip install werkzeug==2.0.3`

## Security Tip
Never use this tool to check real passwords. It's meant for educational purposes only.