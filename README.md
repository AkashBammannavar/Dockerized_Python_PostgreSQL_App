Dockerize Python App — Step-by-step Guide

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


<img width="393" height="374" alt="image" src="https://github.com/user-attachments/assets/825e300d-e3e9-418a-9f42-c597c8d95f8a" />
app.py

<img width="521" height="221" alt="image" src="https://github.com/user-attachments/assets/f3990931-18f5-4cf4-a983-79832444755d" />


4. Build the app image
   Open your terminal

   <img width="497" height="417" alt="image" src="https://github.com/user-attachments/assets/69a8601f-9ec1-441a-addc-5f3c789acf61" />


     Check images:


   <img width="468" height="121" alt="image" src="https://github.com/user-attachments/assets/48b55206-a6eb-4f0e-a396-a0f58872f9f4" />

5. Create a Docker network
    Use a custom network so containers can find each other by name.
   
   <img width="448" height="190" alt="image" src="https://github.com/user-attachments/assets/a211d623-fcea-44ca-8865-e10aba37b493" />

7. Run PostgreSQL container

   docker run -d --name my-postgres --network mynetwork -e POSTGRES_USER=user -e POSTGRES_PASSWORD=pass -e POSTGRES_DB=mydb postgres

   <img width="1008" height="76" alt="image" src="https://github.com/user-attachments/assets/ac968112-2f24-4451-bb19-a29ae2b035bb" />


8. Run the app container (connects to PostgreSQL)
       Run your app on the same network so it can reach Postgres by container name my-postgres:
   
   <img width="752" height="91" alt="image" src="https://github.com/user-attachments/assets/e2ae6dd3-2707-4c6c-9a50-1891409b7995" />


