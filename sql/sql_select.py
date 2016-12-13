import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    output = c.execute("""
    SELECT * FROM employees;
    """)



    for row in output:
        print row[0], row[1]
