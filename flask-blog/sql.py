import sqlite3

with sqlite3.connect("blog.db") as conn:
    c = conn.cursor()
    c.execute("""
    CREATE TABLE posts
    (title TEXT, post TEXT)
    """)

    blog_post = ("Blog Inauguration", "This is my first blog post.")

    c.execute("""
    INSERT INTO posts
    VALUES (?, ?)
    """, blog_post)
