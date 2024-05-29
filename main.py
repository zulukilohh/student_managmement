import tkinter as tk
from tkinter.ttk import Treeview
from students import Person
import tkinter.messagebox as messagebox
#from PIL import ImageTk, Image
from db import Database
from ttkbootstrap import Treeview


class StudentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('student management system')
        self.geometry('450x450')
        self.create_widgets()
        self.configure(bg='lightblue')
        self.database = Database()

    def create_widgets(self):
        # label
        lbl_id = tk.Label(self, text='code meli:', fg='blue')  # font=('Helvetica')
        lbl_id.grid(row=0, column=0, padx=10, pady=10)
        lbl_id.config(bg='lightblue')

        lbl_frist_name = tk.Label(self, text='First name:')
        lbl_frist_name.grid(row=1, column=0, padx=10, pady=10)

        lbl_last_name = tk.Label(self, text='last name:')
        lbl_last_name.grid(row=2, column=0, padx=10, pady=10)

        lbl_age = tk.Label(self, text='age:', bg='green')
        lbl_age.grid(row=3, column=0, padx=10, pady=10)

        lbl_email = tk.Label(self, text='email:')
        lbl_email.grid(row=4, column=0, padx=10, pady=10)

        # entry fields
        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.entry_first_name = tk.Entry(self)
        self.entry_first_name.grid(row=1, column=1, padx=10, pady=10)

        self.entry_last_name = tk.Entry(self)
        self.entry_last_name.grid(row=2, column=1, padx=10)

        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)

        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=4, column=1, padx=10, pady=10)

        # buttons
        btn_add = tk.Button(self, text='add', command=self.add_student, bg='pink')
        btn_add.grid(row=5, column=0, padx=10, pady=10)
        # add_icon = tk.PhotoImage(file="add_icon.png")
        # btn_add.config(image=add_icon, compound="right")

        btn_edit = tk.Button(self, text='edit', command=self.edit_student)
        btn_edit.grid(row=5, column=1, padx=10, pady=10)

        btn_view = tk.Button(self, text='view', command=self.view_student)
        btn_view.grid(row=6, column=0, padx=10, pady=10)

        btn_delete = tk.Button(self, text='delete', command=self.delete_student)
        btn_delete.grid(row=6, column=1, padx=10, pady=10)

        btn_clear = tk.Button(self, text='clear', command=self.clear_entries)
        btn_clear.grid(row=7, column=0, padx=10, pady=10)

        # imageframe
        #image_frame = tk.Frame(self, bg='lightblue')
        #image_frame.grid(row=3, column=3, padx=10, pady=10)

        # image
        # image = Image.open("example.jpg")
        # image = image.resize((100, 100), Image.BICUBIC)
        # photo = ImageTk.PhotoImage(image)
        # self.canvas = tk.Canvas(self, width=100, height=100)
        # self.canvas.grid(row=8, columnspan=2, padx=10, pady=10)
        # self.canvas.create_image(0, 0, anchor=tk.NE, image=photo)
        # label_image = tk.Label(self,image=photo)
        # label_image.image = photo
        # label_image.grid(row=2, columnspan=5, padx=(50, 10), pady=10, sticky='e', )
        # image = Image.open("example.jpg")
        # image = image.resize((100, 100), Image.BICUBIC)
        # photo = ImageTk.PhotoImage(image)
        # label_image = tk.Label(image_frame, image=photo)
        # label_image.image = photo
        # label_image.pack(side='right', padx=(50, 10))
        # spacer_frame = tk.Frame(self, bg='lightblue', width=100)
        # spacer_frame.grid(row=2, column=2, sticky='e')

    def add_student(self):
        meli = self.entry_id.get()
        fist_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()

        if meli and fist_name and last_name and age and email:
            per1 = Person(meli, fist_name, last_name, age, email)
            self.database.add_student(per1)
            self.clear_entries()

        else:
            messagebox.showerror('error', 'Please')

    def edit_student(self):

        # Get the selected student's ID
        student_id = self.entry_id.get()

        # Check if an ID is provided
        if not student_id:
            messagebox.showerror('Error', 'Please enter the student ID to edit.')
            return

        student = (student_id)

        # Check if student exists
        if student:
            # Populate the entry fields with student information
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, student.id)

            self.entry_first_name.delete(0, tk.END)
            self.entry_first_name.insert(0, student.first_name)

            self.entry_last_name.delete(0, tk.END)
            self.entry_last_name.insert(0, student.last_name)

            self.entry_age.delete(0, tk.END)
            self.entry_age.insert(0, student.age)

            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, student.email)

            messagebox.showinfo("Edit Student", "Student information populated for editing.")
        else:
            messagebox.showerror('Error', 'Student not found.')

    def view_student(self):
        view_window = tk.Toplevel(self)
        view_window.title("view students")

        title_label = tk.Label(view_window, text="all student information", font=("Helvetica", 16))
        title_label.pack(pady=10)

        student_grid = Treeview(view_window, columns=("meli", "first_name", "last_name", "age", "email"),
                                show="headings")

        student_grid.heading("meli", text="meli code")
        student_grid.heading("first_name", text="fist name")
        student_grid.heading("last_name", text="last name")
        student_grid.heading("age", text="age")
        student_grid.heading("email", text="email")
        student_grid['show'] = 'headings'

        def on_select(event):
            item_id = student_grid.selection()[0]
            self.select_student = student_grid.item(item_id, 'values')

        student_grid.bind("<<TreeviewSelect>>", on_select)
        
        students = self.database.get_all_students()

        for student in students:
            student_grid.insert("", tk.END, values=student)

        student_grid.pack(fill=tk.BOTH, expand=True)

    def delete_student(self):
        pass

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)


if __name__ == "__main__":
    app = StudentManagementApp()
    app.mainloop()
