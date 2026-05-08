import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
import hashlib
import re
from studentpage import Student
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition
from mainpage import Face_Recognition_System

# ================= LOGIN DATABASE =================
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password12",
        database="login_system"
    )
    cursor = conn.cursor()
except Exception as e:
    print("Database Error:", e)
    

    
# ================= HASH =================
def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()

# ================= VALIDATION =================
def valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def valid_contact(contact):
    return contact.isdigit() and len(contact) == 10

# ================= GRADIENT =================
def create_gradient(canvas, width, height):
    for i in range(height):
        ratio = i / height
        r = int(44 + (86 - 44) * ratio)
        g = int(83 + (171 - 83) * ratio)
        b = int(100 + (47 - 100) * ratio)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)


# =============clearing field========
def clear_login_fields():
    login_user.delete(0, END)
    login_pass.delete(0, END)
    login_user.focus()

# ================= LOGIN FUNCTION =================
def login():
    user = login_user.get().strip()
    pwd = hash_password(login_pass.get().strip())

    if user == "" or login_pass.get() == "":
        messagebox.showerror("Error", "All fields required")
        return

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
    if cursor.fetchone() is not None:
        root.withdraw()
        new_window = tk.Toplevel(root)
        new_window.focus()
        new_window.grab_set()
        app = Face_Recognition_System(new_window,root, clear_login_fields)
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ================= REGISTER PAGE =================
def open_register():
    reg = tk.Toplevel(root)
    reg.attributes("-fullscreen", True)
    

    canvas = tk.Canvas(reg, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    reg.update()
    create_gradient(canvas, reg.winfo_width(), reg.winfo_height())

    frame = tk.Frame(reg, bg="#f8fafc")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=750, height=520)

    tk.Label(frame, text="REGISTER HERE", bg="#f8fafc",
             font=("Segoe UI", 20, "bold")).pack(pady=15)

    form = tk.Frame(frame, bg="#f8fafc")
    form.pack()

    labels = ["Username", "First Name", "Last Name", "Contact", "Email",
              "Security Question", "Security Answer", "Password", "Confirm Password"]

    entries = []

    for i, text in enumerate(labels):
        tk.Label(form, text=text, bg="#f8fafc").grid(row=i//2, column=(i%2)*2, padx=15, pady=10)

        if text == "Security Question":
            entry = ttk.Combobox(form, values=["Pet Name?", "Birth Place?", "Best Friend?"])
            entry.current(0)
        elif "Password" in text:
            entry = tk.Entry(form, show="*")
        else:
            entry = tk.Entry(form)

        entry.grid(row=i//2, column=(i%2)*2+1, padx=15, pady=10)
        entries.append(entry)

    def register_user():
        try:
            data = [e.get() for e in entries]

            if not all(data):
                messagebox.showerror("Error", "All fields required")
                return

            if not valid_contact(data[3]):
                messagebox.showerror("Error", "Invalid Contact Number")
                return

            if not valid_email(data[4]):
                messagebox.showerror("Error", "Invalid Email")
                return

            if data[7] != data[8]:
                messagebox.showerror("Error", "Passwords do not match")
                return

            cursor.execute("SELECT * FROM users WHERE username=%s", (data[0],))
            if cursor.fetchone():
                messagebox.showerror("Error", "Username already exists")
                return

            cursor.execute("""
            INSERT INTO users 
            (username, firstname, lastname, contact, email, security_q, security_a, password)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (data[0], data[1], data[2], data[3], data[4],
            data[5], data[6], hash_password(data[7])))

            conn.commit()
            messagebox.showinfo("Success", "Registered Successfully")
            reg.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    tk.Button(frame, text="Register", bg="#6366f1", fg="white",
              width=20, command=register_user).pack(pady=15)

    tk.Button(frame, text="Back", bg="#22c55e", fg="white",
              width=20, command=reg.destroy).pack()

# ================= MAIN LOGIN UI =================
root = tk.Tk()
root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

root.update()
create_gradient(canvas, root.winfo_width(), root.winfo_height())

frame = tk.Frame(root, bg="#f8fafc")
frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=450)

tk.Label(frame, text="Welcome Back", bg="#f8fafc",
         font=("Segoe UI", 20, "bold")).pack(pady=25)

tk.Label(frame, text="Username", bg="#f8fafc").pack()
login_user = tk.Entry(frame)
login_user.pack(pady=10)

tk.Label(frame, text="Password", bg="#f8fafc").pack()
login_pass = tk.Entry(frame, show="*")
login_pass.pack(pady=10)

tk.Button(frame, text="Login", bg="#6366f1", fg="white",
          width=20, command=login).pack(pady=20)

tk.Button(frame, text="Create Account",
          bg="#f8fafc", fg="#22c55e",
          bd=0, command=open_register).pack()

tk.Button(root, text="X", bg="red", fg="white",
          command=root.destroy).place(x=10, y=10)

root.mainloop()