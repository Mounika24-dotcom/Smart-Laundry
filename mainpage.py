import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Smart Laundry System - Main Page")
root.geometry("300x200")

# UserID label and entry
user_label = tk.Label(root, text="UserID:")
user_label.pack(pady=(20, 5))
user_entry = tk.Entry(root)
user_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=(10, 5))
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Function for login action
def login():
    user_id = user_entry.get()
    password = password_entry.get()
    # Simple check for demonstration
    if user_id == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Incorrect UserID or Password")

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=(10, 5))

# Sign In label and button for new users
new_user_label = tk.Label(root, text="If not registered, New User")
new_user_label.pack(pady=(10, 2))
sign_in_button = tk.Button(root, text="Sign In", command=lambda: messagebox.showinfo("Sign In", "Redirecting to Sign In"))
sign_in_button.pack()

# Run the main loop
root.mainloop()