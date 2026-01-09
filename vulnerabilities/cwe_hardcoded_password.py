# CWE-259: Use of Hard-coded Password

def get_db_password():
    # Vulnerable: hardcoded password
    return "SuperSecret123"
