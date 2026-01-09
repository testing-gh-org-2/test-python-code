# CWE-502: Deserialization of Untrusted Data
import pickle

def insecure_deserialize(data):
    # Vulnerable to arbitrary code execution
    return pickle.loads(data)

# Example usage (vulnerable):
# insecure_deserialize(b'cos
system
(S"calc"
tR.')
