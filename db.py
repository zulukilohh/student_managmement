from tkinter import messagebox

import mysql.connector


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user='root',
            password='20138102',
            database='student_management'
        )
        self.cursor = self.connection.cursor()

    def add_student(self, person):
        try:
            

        except:
            messagebox.showwarning('error', 'Please enter')
