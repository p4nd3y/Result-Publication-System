from tkinter import *
from tkinter import messagebox
import subprocess


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("400x300")

        # Preset login credentials
        self.valid_user_id = "bcet"
        self.valid_password = "bcet@123"

        # Login Page Elements
        Label(self.root, text="Login Page", font=("Arial", 18, "bold")).pack(pady=20)

        Label(self.root, text="User ID", font=("Arial", 14)).place(x=50, y=80)
        self.user_id_var = StringVar()
        Entry(self.root, textvariable=self.user_id_var, font=("Arial", 14)).place(x=150, y=80, width=200)

        Label(self.root, text="Password", font=("Arial", 14)).place(x=50, y=130)
        self.password_var = StringVar()
        Entry(self.root, textvariable=self.password_var, font=("Arial", 14), show="*").place(x=150, y=130, width=200)

        Button(self.root, text="Login", font=("Arial", 14), bg="green", fg="white", command=self.check_login).place(x=80, y=200, width=100)
        Button(self.root, text="Reset Password", font=("Arial", 14), bg="orange", fg="white", command=self.reset_password_page).place(x=220, y=200, width=150)

    def check_login(self):
        user_id = self.user_id_var.get()
        password = self.password_var.get()

        if user_id == self.valid_user_id and password == self.valid_password:
            messagebox.showinfo("Success", "Login Successful")
            self.open_main_program()
        else:
            messagebox.showerror("Error", "Invalid User ID or Password")

    def reset_password_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text="Reset Password", font=("Arial", 18, "bold")).pack(pady=20)

        Label(self.root, text="New User ID", font=("Arial", 14)).place(x=50, y=80)
        self.new_user_id_var = StringVar()
        Entry(self.root, textvariable=self.new_user_id_var, font=("Arial", 14)).place(x=150, y=80, width=200)

        Label(self.root, text="New Password", font=("Arial", 14)).place(x=50, y=130)
        self.new_password_var = StringVar()
        Entry(self.root, textvariable=self.new_password_var, font=("Arial", 14), show="*").place(x=150, y=130, width=200)

        Button(self.root, text="Reset", font=("Arial", 14), bg="green", fg="white", command=self.reset_credentials).place(x=80, y=200, width=100)
        Button(self.root, text="Back", font=("Arial", 14), bg="grey", fg="white", command=self.back_to_login).place(x=220, y=200, width=100)

    def reset_credentials(self):
        new_user_id = self.new_user_id_var.get()
        new_password = self.new_password_var.get()

        if not new_user_id or not new_password:
            messagebox.showerror("Error", "All fields are required")
        else:
            self.valid_user_id = new_user_id
            self.valid_password = new_password
            messagebox.showinfo("Success", "Credentials Updated Successfully")
            self.back_to_login()

    def back_to_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

    def open_main_program(self):
        self.root.destroy()  # Close the login window
        subprocess.Popen(["python", "RPS.py"])  # Open the main program


if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()
