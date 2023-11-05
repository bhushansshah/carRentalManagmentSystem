import tkinter as tk
from tkinter import messagebox

def on_login_click():
    # Dummy check for username and password
    username = entry_username.get()
    password = entry_password.get()
    if username == "user" and password == "pass":  # Replace with your actual check
        show_welcome_screen()
    else:
        messagebox.showerror("Login failed", "Incorrect username or password")

def show_welcome_screen():
    # Clear the existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Show the welcome message
    welcome_label = tk.Label(root, text="Welcome", font=('Helvetica', 18, 'bold'))
    welcome_label.pack(expand=True)

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Set the size of the window
root.geometry('300x150')

# Username Entry
username_label = tk.Label(root, text="Username -")
username_label.pack()

entry_username = tk.Entry(root)
entry_username.pack()

# Password Entry
password_label = tk.Label(root, text="Password -")
password_label.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Login Button
login_button = tk.Button(root, text="LOGIN", command=on_login_click)
login_button.pack()

# Signup Button
signup_button = tk.Button(root, text="SIGNUP") # You need to add the functionality for signup
signup_button.pack()

root.mainloop()
