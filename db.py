import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user='root',
            password='20138102',
            database='student_management'
        )
        