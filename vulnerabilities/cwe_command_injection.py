# CWE-77: Improper Neutralization of Special Elements used in a Command ('Command Injection')
import os

def unsafe_system_call(user_input):
    # Vulnerable to command injection
    os.system('echo ' + user_input)

# Example usage (vulnerable):
# unsafe_system_call('hello && dir')
