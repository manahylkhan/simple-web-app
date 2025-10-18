# app.py
import os
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    # Retrieve connection details from environment variables/secrets
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    
    # Docker secrets are mounted as files in /run/secrets/
    try:
        with open("/run/secrets/db_user", "r") as f:
            DB_USER = f.read().strip()
        with open("/run/secrets/db_password", "r") as f:
            DB_PASSWORD = f.read().strip()
        with open("/run/secrets/db_name", "r") as f:
            DB_NAME = f.read().strip()
    except FileNotFoundError:
        return "<h1>Error: Database secrets not found!</h1>"

    # Attempt to connect to the database
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        return "<h1>Web App is Running and Connected to PostgreSQL! ✅</h1>"
    except Exception as e:
        return f"<h1>Web App is Running but FAILED to Connect to DB: ❌</h1><p>{e}</p>"

if __name__ == '__main__':
    # Flask's default port is 5000, but we'll use 8000 for Docker
    app.run(host='0.0.0.0', port=8000)
