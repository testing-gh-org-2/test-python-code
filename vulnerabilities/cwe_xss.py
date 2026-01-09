# CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
from flask import Flask, request
app = Flask(__name__)

@app.route('/xss')
def xss():
    name = request.args.get('name', '')
    # Vulnerable to reflected XSS
    return f'<h1>Hello {name}</h1>'

# Example usage: /xss?name=<script>alert(1)</script>
