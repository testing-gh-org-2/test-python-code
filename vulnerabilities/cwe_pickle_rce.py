# CWE-502: Deserialization of Untrusted Data (Pickle RCE)
import pickle

def pickle_rce(payload):
    # Vulnerable: unsafe pickle.loads
    return pickle.loads(payload)
