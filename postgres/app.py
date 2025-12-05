import psycopg2
import time

time.sleep(5)

try:
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass"
    )

    cur = conn.cursor()

    # Create table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name TEXT,
            course TEXT
        )
    """)

    # Insert record
    cur.execute("INSERT INTO students (name, course) VALUES (%s, %s)", ("Akash", "Docker"))

    conn.commit()

    # Read data
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    print("Database Records:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)
