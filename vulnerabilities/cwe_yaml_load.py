# CWE-502: Deserialization of Untrusted Data (PyYAML load)
import yaml

def yaml_load(data):
    # Vulnerable: yaml.load without Loader
    return yaml.load(data)
