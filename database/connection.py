import mysql.connector

class Database:
    def connect(self):
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1234',
            database = 'test'
        )
        return conn