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
            query = "INSERT INTO students (meli, first_name, last_name, age, email) VALUES (%s, %s, %s, %s, %s)"
            person = (person.meli, person.first_name, person.last_name, person.age, person.email)
            self.cursor.execute(query, person)
            self.connection.commit()
            messagebox.showinfo("Student added", "Student")
        except Exception as e:
            print(e)
            messagebox.showwarning('error', 'Please enter')


    def get_all_students(self):
        try:
            query = "SELECT * FROM students"
            self.cursor.execute(query)
            students = self.cursor.fetchall()
            return students
        except mysql.connector.Error as err:
            messagebox.showerror("error", f"Error while connecting to MySQL: {err}")
            return None