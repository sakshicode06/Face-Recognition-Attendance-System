from tkinter import*
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk   #to crop image
import os
from time import strftime
from tkinter import Toplevel
from datetime import datetime
from studentpage import Student
from face_recognition import Face_Recognition
from train import Train
from attendance import Attendance
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np





class Face_Recognition_System:
    
    def clear_frame(self):
     for widget in self.root.winfo_children():
        widget.destroy()
        
    def show_main(self):
        self.clear_frame()
        self.__init__(self.root, self.login_window, self.clear_func)
    
      # reload main UI
    def __init__(self,root,login_window, clear_func):
        self.root=root
        self.login_window = login_window
        self.clear_func = clear_func
        self.root.state('zoomed')   # FULL SCREEN
        self.root.title("Face Recognition System")
        self.root.configure(bg="#eef2f7")

        # ===== HEADER =====
        header = Frame(self.root, bg="#2c3e50")
        header.pack(fill=X)

        title = Label(header,
                      text="Face Recognition Attendance System",
                      font=("Segoe UI", 26, "bold"),
                      bg="#2c3e50",
                      fg="white")
        title.pack(side=LEFT, padx=20, pady=15)

        # clock
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(header,
                    font=("Segoe UI", 12, "bold"),
                    bg="#2c3e50",
                    fg="#f1c40f")
        lbl.pack(side=RIGHT, padx=20)
        time()

        # ===== MAIN FRAME =====
        self.container = Frame(self.root, bg="#eef2f7")
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_rowconfigure(1, weight=1)

        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_columnconfigure(2, weight=1)
        self.load_main_cards()

        # ===== FUNCTION TO CREATE CARD =====
        


        # ===== CARDS =====
    def load_main_cards(self):
        def create_card(row, col, img_path, text, command, color):
             img = Image.open(img_path)
             img = img.resize((100, 100), Image.Resampling.LANCZOS)
             photo = ImageTk.PhotoImage(img)

             card = Frame(self.container, bg="white", bd=2, relief=RIDGE)
             card.grid(row=row, column=col, padx=50, pady=40)

             btn = Button(card, image=photo, command=command,
                     bd=0, bg="white", activebackground="white", cursor="hand2")
             btn.image = photo
             btn.pack(padx=20, pady=10)

             label = Label(card, text=text,
                      font=("Segoe UI", 13, "bold"),
                      bg="white", fg=color)
             label.pack(pady=10)

    # CARDS
        create_card(0, 0, r"images/student icon.webp", "Student Details", self.student_details, "#2c3e50")
        create_card(0, 1, r"images/face detection.jpg", "Face Detector", self.face_data, "#2980b9")
        create_card(0, 2, r"images/student_img.png", "Attendance", self.attendance_data, "#27ae60")

        create_card(1, 0, r"images/train_data.jpg", "Train Data", self.train_data, "#8e44ad")
        create_card(1, 1, r"images/student_img.png", "Photos", self.open_img, "#16a085")
        create_card(1, 2, r"images/exit-icon.jpg", "Logout", self.iExit, "#e74c3c")
         # ***********functions button*****************
    def open_img(self):
        os.startfile("data")
    def iExit(self):
        if messagebox.askyesno("Exit", "Do you want to logout?", parent=self.root):
            self.root.destroy()            # close dashboard
            self.clear_func()
            self.login_window.deiconify()  # show login again
         
    
    def student_details(self):
        print("Student button clicked")   # DEBUG
        self.clear_frame()
        self.app = Student(self.root,self.show_main)
        
    def train_data(self):
        self.clear_frame()
        self.app = Train(self.root,self.show_main)
    
    def face_data(self):
        self.clear_frame()
        self.app = Face_Recognition(self.root,self.show_main)

        
    def attendance_data(self):
        self.clear_frame()
        self.app = Attendance(self.root,self.show_main)
        
    

# if __name__ == "__main__":      #
#     root=Tk()                   #call root from toolkit
#     obj=Face_Recognition_System(root,root)        #making classs object
#     root.mainloop()