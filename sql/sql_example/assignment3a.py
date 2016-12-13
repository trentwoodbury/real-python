import sqlite3
import numpy as np

rand_nums = np.random.choice(100, 100)

with sqlite3.connect("newnum.db") as conn:
    c = conn.cursor()
    # c.execute("""
    # CREATE TABLE numbers
    # (num INT);
    # """)

    for i in range(100):
        c.execute("""
        INSERT INTO numbers(num)
        VALUES (?)
        """, (rand_nums[i], ))
