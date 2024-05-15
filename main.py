import tkinter as tk
from students import Person
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image

class StudentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('student management system')
        self.geometry('450x450')
        self.create_widgets()
        self.configure(bg='lightblue')

    def create_widgets(self):
        # label
        lbl_id = tk.Label(self, text='code meli:', fg='blue') #font=('Helvetica')
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
        #add_icon = tk.PhotoImage(file="add_icon.png")
        #btn_add.config(image=add_icon, compound="right")

        btn_edit = tk.Button(self, text='edit', command=self.edit_student)
        btn_edit.grid(row=5, column=1, padx=10, pady=10)

        btn_view = tk.Button(self, text='view', command=self.view_student)
        btn_view.grid(row=6, column=0, padx=10, pady=10)

        btn_delete = tk.Button(self, text='delete', command=self.delete_student)
        btn_delete.grid(row=6, column=1, padx=10, pady=10)

        btn_clear = tk.Button(self, text='clear', command=self.clear_entries)
        btn_clear.grid(row=7, column=0, padx=10, pady=10)

        #imageframe
        image_frame = tk.Frame(self, bg='lightblue')
        image_frame.grid(row=2, column=1, padx=10, pady=10)

        #image
        image = Image.open("example.jpg")
        image = image.resize((100, 100), Image.BICUBIC)
        photo = ImageTk.PhotoImage(image)
        #self.canvas = tk.Canvas(self, width=100, height=100)
        #self.canvas.grid(row=8, columnspan=2, padx=10, pady=10)
        #self.canvas.create_image(0, 0, anchor=tk.NE, image=photo)
        label_image = tk.Label(self, image=photo)
        label_image.image = photo
        label_image.grid(row=2, columnspan=5, padx=(50,10), pady=10, sticky='e',)
        #image = Image.open("example.jpg")
        #image = image.resize((100, 100), Image.BICUBIC)
        #photo = ImageTk.PhotoImage(image)
        #label_image = tk.Label(image_frame, image=photo)
        #label_image.image = photo
        #label_image.pack(side='right', padx=(50, 10))
        #spacer_frame = tk.Frame(self, bg='lightblue', width=100)
        #spacer_frame.grid(row=2, column=2, sticky='e')
    def add_student(self):
        meli = self.entry_id.get()
        fist_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()

        if meli and fist_name and last_name and age and email:
            per1 = Person(meli, fist_name, last_name, age, email)
            messagebox.showinfo("success", "Student added!")
            self.clear_entries()
        else:
            messagebox.showerror('error', 'Please')

    def edit_student(self):
        pass

    def view_student(self):
        pass

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
