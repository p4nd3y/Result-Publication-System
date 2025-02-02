import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox

class ResultPublicationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Publication System")
        self.root.geometry("1500x800")

        # Variables for entries
        self.var_student_id = StringVar()
        self.var_roll_number = StringVar()
        self.var_student_name = StringVar()
        self.var_class = StringVar()
        self.var_total_marks = StringVar()
        self.var_marks_obtained = StringVar()
        self.var_percentage = StringVar()
        self.var_result = StringVar()

        # Title
        title = Label(self.root, text="Result Publication System", font=('arial', 40, 'bold'), bg="crimson", fg="white", bd=10, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # Frame for form
        frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        frame.place(x=20, y=100, width=450, height=600)

        # Labels and Entries
        Label(frame, text="Student ID", font=('arial', 14, 'bold'), bg='white').grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ttk.Entry(frame, textvariable=self.var_student_id, font=('arial', 13, 'bold'), width=20).grid(row=0, column=1, padx=10, pady=10)

        Label(frame, text="Roll Number", font=('arial', 14, 'bold'), bg='white').grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ttk.Entry(frame, textvariable=self.var_roll_number, font=('arial', 13, 'bold'), width=20).grid(row=1, column=1, padx=10, pady=10)

        Label(frame, text="Student Name", font=('arial', 14, 'bold'), bg='white').grid(row=2, column=0, padx=10, pady=10, sticky="w")
        ttk.Entry(frame, textvariable=self.var_student_name, font=('arial', 13, 'bold'), width=20).grid(row=2, column=1, padx=10, pady=10)

        Label(frame, text="Class", font=('arial', 14, 'bold'), bg='white').grid(row=3, column=0, padx=10, pady=10, sticky="w")
        class_combo = ttk.Combobox(frame, textvariable=self.var_class, font=('arial', 13, 'bold'), width=18, state='readonly')
        class_combo['values'] = ('Nursery', 'KG', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        class_combo.current(0)
        class_combo.grid(row=3, column=1, padx=10, pady=10)

        Label(frame, text="Total Marks", font=('arial', 14, 'bold'), bg='white').grid(row=4, column=0, padx=10, pady=10, sticky="w")
        ttk.Entry(frame, textvariable=self.var_total_marks, font=('arial', 13, 'bold'), width=20).grid(row=4, column=1, padx=10, pady=10)

        Label(frame, text="Marks Obtained", font=('arial', 14, 'bold'), bg='white').grid(row=5, column=0, padx=10, pady=10, sticky="w")
        ttk.Entry(frame, textvariable=self.var_marks_obtained, font=('arial', 13, 'bold'), width=20).grid(row=5, column=1, padx=10, pady=10)

        # Buttons for operations
        Button(frame, text="Add Result", command=self.add_data, font=('arial', 12, 'bold'), width=18, bg='blue', fg='white').grid(row=6, column=0, padx=10, pady=20)
        Button(frame, text="Update Result", command=self.update_data, font=('arial', 12, 'bold'), width=18, bg='green', fg='white').grid(row=6, column=1, padx=10, pady=20)
        Button(frame, text="Delete Result", command=self.delete_data, font=('arial', 12, 'bold'), width=18, bg='red', fg='white').grid(row=7, column=0, padx=10, pady=20)
        Button(frame, text="Clear", command=self.clear_data, font=('arial', 12, 'bold'), width=18, bg='grey', fg='white').grid(row=7, column=1, padx=10, pady=20)

        # Frame for searching
        search_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=500, y=100, width=900, height=60)

        Label(search_frame, text="Search By", font=('arial', 12, 'bold'), bg="white").grid(row=0, column=0, padx=10, pady=10)
        self.var_com_search = StringVar()
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=('arial', 11, 'bold'), width=18, state='readonly')
        search_combo['value'] = ('Select Option', 'student_id', 'roll_number', 'class')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5)

        self.var_search = StringVar()
        ttk.Entry(search_frame, textvariable=self.var_search, font=('arial', 11, 'bold'), width=18).grid(row=0, column=2, padx=5)
        Button(search_frame, command=self.search_data, text="Search", font=('arial', 13, 'bold'), width=14, bg="blue", fg="white").grid(row=0, column=3, padx=5)
        Button(search_frame, command=self.fetch_data, text="Show All", font=('arial', 13, 'bold'), width=14, bg="blue", fg="white").grid(row=0, column=4, padx=5)

        # Table for displaying results
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=500, y=180, width=900, height=500)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.result_table = ttk.Treeview(table_frame, column=('1', '2', '3', '4', '5', '6', '7', '8'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.result_table.xview)
        scroll_y.config(command=self.result_table.yview)

        # Table headings
        headings = ['Student ID', 'Roll Number', 'Student Name', 'Class', 'Total Marks', 'Marks Obtained', 'Percentage', 'Result']
        for i, heading in enumerate(headings, start=1):
            self.result_table.heading(str(i), text=heading)
            self.result_table.column(str(i), width=100)
        self.result_table['show'] = 'headings'
        self.result_table.pack(fill=BOTH, expand=1)
        self.result_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()  # Initial load

    def add_data(self):
        if self.var_student_id.get() == '':
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                total_marks = float(self.var_total_marks.get())
                marks_obtained = float(self.var_marks_obtained.get())
                percentage = (marks_obtained / total_marks) * 100
                result = "Pass" if percentage >= 50 else "Fail"

                conn = mysql.connector.connect(host='localhost', username='root', password='141111', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('''INSERT INTO results (student_id, roll_number, student_name, class, total_marks, marks_obtained, percentage, result) 
                                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', (
                    self.var_student_id.get(),
                    self.var_roll_number.get(),
                    self.var_student_name.get(),
                    self.var_class.get(),
                    total_marks,
                    marks_obtained,
                    f"{percentage:.2f}",
                    result
                ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}")

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='141111', database='management')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM results")
        rows = my_cursor.fetchall()
        if rows:
            self.result_table.delete(*self.result_table.get_children())
            for row in rows:
                self.result_table.insert('', END, values=row)
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.result_table.focus()
        contents = self.result_table.item(cursor_row)
        row = contents['values']
        self.var_student_id.set(row[0])
        self.var_roll_number.set(row[1])
        self.var_student_name.set(row[2])
        self.var_class.set(row[3])
        self.var_total_marks.set(row[4])
        self.var_marks_obtained.set(row[5])
        self.var_percentage.set(row[6])
        self.var_result.set(row[7])

    def update_data(self):
        if self.var_student_id.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
        else:
            try:
                total_marks = float(self.var_total_marks.get())
                marks_obtained = float(self.var_marks_obtained.get())
                percentage = (marks_obtained / total_marks) * 100
                result = "Pass" if percentage >= 50 else "Fail"

                conn = mysql.connector.connect(host='localhost', username='root', password='141111', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('''UPDATE results SET roll_number=%s, student_name=%s, class=%s, 
                                     total_marks=%s, marks_obtained=%s, percentage=%s, result=%s WHERE student_id=%s''', (
                    self.var_roll_number.get(),
                    self.var_student_name.get(),
                    self.var_class.get(),
                    total_marks,
                    marks_obtained,
                    f"{percentage:.2f}",
                    result,
                    self.var_student_id.get()
                ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been updated successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}")

    def delete_data(self):
        if self.var_student_id.get() == "":
            messagebox.showerror("Error", "Please select a record to delete")
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='141111', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM results WHERE student_id=%s", (self.var_student_id.get(),))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been deleted successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}")

    def clear_data(self):
        self.var_student_id.set("")
        self.var_roll_number.set("")
        self.var_student_name.set("")
        self.var_class.set("")
        self.var_total_marks.set("")
        self.var_marks_obtained.set("")
        self.var_percentage.set("")
        self.var_result.set("")

    def search_data(self):
        if self.var_com_search.get() == "Select Option" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select a search option and enter a search term")
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='141111', database='management')
                my_cursor = conn.cursor()
                query = f"SELECT * FROM results WHERE {self.var_com_search.get()} LIKE '%{self.var_search.get()}%'"
                my_cursor.execute(query)
                rows = my_cursor.fetchall()
                if rows:
                    self.result_table.delete(*self.result_table.get_children())
                    for row in rows:
                        self.result_table.insert('', END, values=row)
                else:
                    messagebox.showinfo("Info", "No matching records found")
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}")

# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = ResultPublicationSystem(root)
    root.mainloop()
