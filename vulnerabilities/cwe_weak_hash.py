# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
import hashlib

def weak_hash(data):
    # Vulnerable: MD5 is not secure
    return hashlib.md5(data.encode()).hexdigest()

# Example usage (vulnerable):
# weak_hash('password')
