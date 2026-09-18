import os
import mysql.connector

class Database:
    def connect(self):
        conn = mysql.connector.connect(
            host = os.getenv("DB_HOST", "localhost"),
            user = os.getenv("DB_USER", "root"),
            password = os.getenv("DB_PASSWORD", "1234"),
            database = os.getenv("DB_NAME", "test")
        )
        return conn
