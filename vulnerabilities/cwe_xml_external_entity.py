# CWE-611: Improper Restriction of XML External Entity Reference ('XXE')
import lxml.etree

def parse_xml(data):
    # Vulnerable to XXE
    return lxml.etree.fromstring(data)

# Example usage (vulnerable):
# parse_xml(b'<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>')
