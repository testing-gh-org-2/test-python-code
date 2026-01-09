# CWE-94: Improper Control of Generation of Code ('Code Injection')
def eval_injection(user_code):
    # Vulnerable: eval on user input
    return eval(user_code)
