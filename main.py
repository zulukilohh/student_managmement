import tkinter as tk

class StudentManagementApp(tk.TK):
    def __init__(self):
        super().__init__()

        self.title('student management system')
        self.geometry('250x400')
        self.create_widgets()


if __name__ == "__main__":
    app = StudentManagementApp()
    app.mainloop()







