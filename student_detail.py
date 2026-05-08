from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import messagebox              #to show message
import mysql.connector
import traceback
import cv2
import time
import os

class Student:

    def __init__(self, root, back_callback=None ):
        self.root = root    
        self.back_callback = back_callback #geometry of lap. resolution,x,y
        self.root.title("face Recognition System")
        
        # ==================variables====================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()
        
        #screen_width=self.root.winfo_screenwidth()
        #screen_height= self.root.winfo_screenheight()
        #img=Image.open(r"C:\Users\mramz\OneDrive\Desktop\face_recognition_system\images\blackbg.avif")
        #img=img.resize((screen_width,screen_height),Image.Resampling.LANCZOS)
        #self.photoimg=ImageTk.PhotoImage(img)
            
        #f_lbl=Label(self.root,image=self.photoimg)
        #f_lbl.place(x=0, y=0, relwidth=1, relheight=1)
            
        title_label=Label(self.root,
          text="STUDENT MANAGEMENT SYSTEM",
          font=("times new roman",35,"bold"),
          fg="#C2D3DA",
          bg="#4a4a4a",
          bd=5,
          relief="ridge"
        )
        title_label.place(x=0, y=0, relwidth=1, height=60)  
        
        back_btn = Button(self.root,
                  text="← Back",
                  command=self.back_callback,
                  font=("times new roman", 12, "bold"),
                  bg="#4a4a4a",
                  fg="white")

        back_btn.place(x=10, y=10)  
            
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=10, y=70, width=1260, height=600)
            
        #left label frame
            
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))  #left table for student detail
        Left_frame.place(x=10,y=10,width=600,height=550)
            
        img_left=Image.open(r"C:\Users\mramz\OneDrive\Desktop\face_recognition_system\images\student_img.png")
        img_left=img_left.resize((580,90),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
            
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=580,height=90)
        
        
            
            
        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))  #left table for student detail
        current_course_frame.place(x=5,y=95,width=585,height=125)
            
            #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        dep_label.grid(row=0,column=0,padx=8,sticky=W)
            
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only",width=20)   #departemt combo box
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=6,sticky=W)
            
            #course
            
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        course_label.grid(row=0,column=2,padx=10,sticky=W)
            
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=20)   #departemt combo box
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
            
            #year
            
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        year_label.grid(row=1,column=0,padx=10,sticky=W)
            
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=20)   #departemt combo box
        year_combo["values"]=("Select Year","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
            
            #Semester
            
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
            
        div_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only",width=20)   #departemt combo box
        div_combo["values"]=("Select Semester","Sem-1","Sem-2")
        div_combo.current(0)
        div_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
            
            #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))  #left table for student detail
        class_student_frame.place(x=5,y=230,width=585,height=290)
            
            #student id
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        studentId_label.grid(row=0,column=0,padx=4,pady=3,sticky=W)
            
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=17,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=4,pady=3,sticky=W)
            
            #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        studentName_label.grid(row=0,column=2,padx=4,pady=3,sticky=W)
            
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=17,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=4,pady=3,sticky=W)
            
            #class division
        student_div_label=Label(class_student_frame,text="Student Division:",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        student_div_label.grid(row=1,column=0,padx=4,pady=3,sticky=W)
            
        # student_div_entry=ttk.Entry(class_student_frame,textvariablself.var_div,width=17,font=("times new roman",12,"bold"))
        # student_div_entry.grid(row=1,column=1,padx=4,pady=3,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=15)   #departemt combo box
        div_combo["values"]=("Select Division","NONE","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=4,pady=3,sticky=W)
        
        #Roll no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        roll_no_label.grid(row=1,column=2,padx=4,pady=3,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=17,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=4,pady=3,sticky=W)
        
        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        gender_label.grid(row=2,column=0,padx=4,pady=3,sticky=W)
        
        # gender_entry=ttk.Entry(class_student_frame,textvariablself.var_gender,width=17,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=4,pady=3,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=15)   #departemt combo box
        div_combo["values"]=("Gender","Male","Female","Other")
        div_combo.current(0)
        div_combo.grid(row=2,column=1,padx=4,pady=3,sticky=W)
        
        #Date of birth
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        dob_label.grid(row=2,column=2,padx=4,pady=3,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=17,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=4,pady=3,sticky=W)
        
        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")   #for department in current course info
        email_label.grid(row=3,column=0,padx=4,pady=3,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=17,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=4,pady=3,sticky=W)
        
        #phone no
        phone_label=Label(class_student_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")   
        phone_label.grid(row=3,column=2,padx=4,pady=3,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=17,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=4,pady=3,sticky=W)
        
        #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")   
        address_label.grid(row=4,column=0,padx=4,pady=3,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=17,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=5,pady=3,sticky=W)
        
        #Teacher name
        
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")   
        teacher_label.grid(row=4,column=2,padx=4,pady=3,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=17,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=4,pady=3,sticky=W)
        
        #radio buttons
        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,text="take a photo sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,text="NO photo sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=5,column=2,padx=5,pady=5,sticky=W)        
        
        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=185,width=585,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="#4a4a4a",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="#4a4a4a",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="#4a4a4a",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="#4a4a4a",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=220,width=585,height=35)
        
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take a photo sample",width=32,font=("times new roman",12,"bold"),bg="#4a4a4a",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,command=self.update_photo_sample,text="Update a photo sample",width=32,font=("times new roman",12,"bold"),bg="#4a4a4a",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        
        
         #right label frame
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=620,y=10,width=630,height=550)
        
        img_right=Image.open(r"C:\Users\mramz\OneDrive\Desktop\face_recognition_system\images\student_img.png")
        img_right=img_right.resize((610,90),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=610,height=90)
        
        #=============Search System==================
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))  #left table for student detail
        Search_frame.place(x=5,y=95,width=620,height=80)
        
        search_label=Label(Search_frame,text="Search by:",font=("times new roman",12,"bold"),bg="#4a4a4a",fg="white")   
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_search_by,font=("times new roman",12,"bold"),state="read only",width=15)   #departemt combo box
        search_combo["values"]=("Select","Name","Roll")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search_txt,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(Search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",11,"bold"),bg="#4a4a4a",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(Search_frame,text="Show ALL",command=self.fetch_data,width=12,font=("times new roman",11,"bold"),bg="#4a4a4a",fg="white")
        showAll_btn.grid(row=0,column=4) 
        
        #============TABLE FRAME=========================    
        Table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)  #left table for student detail
        Table_frame.place(x=5,y=180,width=620,height=350)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(Table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
            
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=200)
        self.student_table.column("course",width=200)
        self.student_table.column("year",width=200)
        self.student_table.column("sem",width=200)
        self.student_table.column("id",width=200)
        self.student_table.column("name",width=200)
        self.student_table.column("div",width=200)
        self.student_table.column("roll",width=200)
        self.student_table.column("gender",width=200)
        self.student_table.column("dob",width=200)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=200)
        self.student_table.column("address",width=200)
        self.student_table.column("teacher",width=200)
        self.student_table.column("photo",width=200)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # ====================function declaration========================
    
    # save 
    def add_data(self):
        # print("ADD_DATA CALLED")
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                # save data in D.B.
                conn=mysql.connector.connect(host="localhost",username="root",password="password12",database="face_recognizer")
                my_cursor=conn.cursor()
                # executing my sql query everything is varchar and student 
                my_cursor.execute("SELECT * FROM student WHERE student_id=%s", (self.var_std_id.get(),))
                # check duplicatemstudent id
                result = my_cursor.fetchone()

                if result:
                    messagebox.showerror("Error", "Student ID already exists", parent=self.root)
                    return
                my_cursor.execute("insert into student (Dep, course, Year, Semester, student_id, Name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()
                                                                                        
                                                                                                            ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due To : {str(traceback.format_exc())}",parent=self.root)
            
    #========================fetching data from database to table=======================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password12",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    
    # ===========get cursor==============   getting data in entry field when click on row
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        # check if row is empty
        if not data:
            return
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    # update func
    def update_data(self):
        # validation
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the student details?",parent=self.root)
                if Update>0:
                    # creating  connection
                    conn=mysql.connector.connect(host="localhost",username="root",password="password12",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                        
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                               
                                                                                                                                                                                                                                                 ))
                else:   
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(traceback.format_exc())}",parent=self.root)
                        
    # delete func
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Do you want to delete the student",parent=self.root)
                if Delete>0:
                    student_id = self.var_std_id.get()
                    # creating  connection
                    conn=mysql.connector.connect(host="localhost",username="root",password="password12",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    # val=(self.var_std_id.get(),)
                    # my_cursor.execute(sql,val)
                    my_cursor.execute(sql, (student_id,))
                    conn.commit()
                    conn.close()
                    # DELETE IMAGES FROM FOLDER
                    for file in os.listdir("data"):
                        if file.startswith(f"user.{student_id}."):
                            os.remove(os.path.join("data", file))
                    # REFRESH TABLE + CLEAR FORM
                    self.fetch_data()
                    self.reset_data()
                    messagebox.showinfo("Delete","Student deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(traceback.format_exc())}",parent=self.root)
                
    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
        
    #===========Generate data set or take photo samples=================
    def generate_dataset(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
        # else:
            student_id = self.var_std_id.get().strip()
            if student_id == "":
                messagebox.showerror("Error", "Please enter Student ID first", parent=self.root)
                return
            try:
                # creating  connection
                conn=mysql.connector.connect(host="localhost",username="root",password="password12",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                # id=0
                # for x in myresult:
                #     id+=1
                my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                        
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                 ))          
                conn.commit() 
                self.fetch_data()
                self.reset_data()
                conn.close()          
                 
                 #==========Load predefined data on face frontals from opencv===========
                 
                
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                 
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                     #scaling factor=1.3
                     #minimum meighbour=5
                     
                    for (x,y,w,h) in faces:
                         face_cropped=img[y:y+h,x:x+w]
                         return face_cropped
                     
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                     ret,my_frame=cap.read()
                     if face_cropped(my_frame) is not None:
                         img_id+=1
                         face=cv2.resize(face_cropped(my_frame),(450,450) ) 
                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        #  file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                         file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("Cropped face",face)
            
                     if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(traceback.format_exc())}",parent=self.root)
                                  
    # ===============search data===============
    def search_data(self):
        if self.var_search_by.get() == "Select" or self.var_search_txt.get() == "":
            messagebox.showerror("Error", "Please select search option and enter value", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="password12",database="face_recognizer")
                my_cursor = conn.cursor()

                if self.var_search_by.get() == "Name":
                    query = "SELECT * FROM student WHERE Name LIKE %s"
                elif self.var_search_by.get() == "Roll":
                    query = "SELECT * FROM student WHERE Roll LIKE %s"

                my_cursor.execute(query, ('%' + self.var_search_txt.get() + '%',))
                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                else:
                    messagebox.showinfo("Result", "No Record Found", parent=self.root)

                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(traceback.format_exc())}", parent=self.root)
                                                                                           
    #=====================update photo sample ==============
    def update_photo_sample(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID required", parent=self.root)
            return

        try:
            student_id = self.var_std_id.get()

            #DELETE OLD IMAGES
            for file in os.listdir("data"):
                if file.startswith(f"user.{student_id}."):
                    os.remove(os.path.join("data", file))

            messagebox.showinfo("Info", "Old photos deleted")

            # CALL CAMERA AGAIN
            self.generate_dataset()

        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self.root)
                                   
                                   
if __name__ == "__main__":      #
   root=Tk()                   #call root from toolkit
   obj=Student(root)        #making classs object
   root.mainloop()