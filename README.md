<img width="393" height="374" alt="image" src="https://github.com/user-attachments/assets/825e300d-e3e9-418a-9f42-c597c8d95f8a" />Dockerize Python App — Step-by-step Guide

This repository shows how to Dockerize a simple Python app that connects to PostgreSQL, creates a table, inserts a row, and reads it back. It includes commands for Windows PowerShell and Linux , Dockerfile, app.py, networking, troubleshooting and instructions for adding screenshots to the repo.

Repository structure
projectDocker/
├── app.py
├── Dockerfile
├── README.md <-- this file
├── screenshots/
│ ├── docker-desktop.png
│ ├── docker-images.png
│ ├── docker-ps.png
│ └── postgres-running.png
└── .gitignore

1. Project purpose
his project demonstrates:
    Creating a simple Python script (app.py) that uses psycopg2 to talk to PostgreSQL.
    Writing a Dockerfile and building a Docker image for the app.
    Creating a custom Docker network and running a PostgreSQL container connected to it.
    Running the Python app container on the same network and verifying the DB operations.

2. Prerequisites
  Docker Desktop installed and running (Windows/macOS) or Docker Engine (Linux).
  Download: https://www.docker.com/products/docker-desktop
  Git installed.
  Basic knowledge of terminal/VS CODE

3.Files(Code)
app.py

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

cur.execute("INSERT INTO students (name, course) VALUES (%s, %s)", ("Akash", "Docker"))

conn.commit()
cur.execute("SELECT * FROM students")
rows = cur.fetchall()

print("Database Records:")
for row in rows:
print(row)

cur.close()
conn.close()

except Exception as e:
print("Error:", e)
