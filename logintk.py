import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Chandana67',
    database='tkinter_db'
)
cursor = conn.cursor()


#  Login User 
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute("SELECT * FROM userlogin WHERE username=%s AND password=%s",
                   (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", f"Welcome {username}! Login Successful")
    else:
        messagebox.showerror("Failed", "Invalid Username or Password")

#  UI 
root = tk.Tk()
root.title("User Login")
root.geometry("350x250")

tk.Label(root, text="Login System", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

btn_login = tk.Button(root, text="Login", width=10, command=login_user)
btn_login.pack(pady=5)



root.mainloop()
