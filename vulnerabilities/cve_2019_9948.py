# CVE-2019-9948: Python urllib SSRF vulnerability
import urllib.request

def ssrf_vulnerable(url):
    # Vulnerable to SSRF in Python < 3.7.4
    with urllib.request.urlopen(url) as response:
        return response.read()

# Example usage (vulnerable):
# ssrf_vulnerable('file:///etc/passwd')
