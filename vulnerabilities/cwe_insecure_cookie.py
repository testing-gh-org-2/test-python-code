# CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute
from flask import Flask, make_response
app = Flask(__name__)

@app.route('/setcookie')
def setcookie():
    resp = make_response('Setting cookie!')
    # Vulnerable: missing secure flag
    resp.set_cookie('sessionid', '12345')
    return resp
