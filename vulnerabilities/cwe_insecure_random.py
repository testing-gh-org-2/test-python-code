# CWE-338: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
import random

def insecure_token():
    # Vulnerable: random is not secure for tokens
    return random.randint(100000, 999999)
