# CWE-918: Server-Side Request Forgery (SSRF)
import requests

def ssrf(url):
    # Vulnerable: user-controlled URL
    return requests.get(url).text
