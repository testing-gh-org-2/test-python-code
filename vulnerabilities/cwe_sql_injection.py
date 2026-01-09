# CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
import sqlite3

def unsafe_query(user_input):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (id INTEGER, name TEXT)')
    cursor.execute("INSERT INTO users VALUES (1, 'admin')")
    # Vulnerable to SQL Injection
    query = "SELECT * FROM users WHERE name = '%s'" % user_input
    cursor.execute(query)
    return cursor.fetchall()

# Example usage (vulnerable):
# unsafe_query("' OR '1'='1")
