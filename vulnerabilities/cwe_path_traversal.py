# CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
from flask import Flask, request, send_file
import os
app = Flask(__name__)

@app.route('/file')
def file():
    filename = request.args.get('filename', '')
    # Vulnerable to path traversal
    return send_file(os.path.join('uploads', filename))

# Example usage: /file?filename=../../etc/passwd
