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





class Face_Recognition:
    def __init__(self,root, back_callback):
        self.root=root    #initialize root
        self.back_callback = back_callback   #geometry of lap. resolution,x,y
        self.root.title("face Recognition System")
        
        # get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        title_lbl=Label(self.root,text="FACE RECOGNITION ",font=('times new roman',35,"bold"),fg="white",bg="#05407A")
        title_lbl.place(x=0,y=0,relwidth=1,height=55)
          
        back_btn = Button(self.root,
                  text="← Back",
                  command=self.back_callback,
                  font=("times new roman",12,"bold"),
                  bg="#05407A",
                  fg="white",
                  cursor="hand2")
        back_btn.place(x=10, y=10)
        
        # adding 1st images
        img1=Image.open(r"C:\Users\mramz\OneDrive\Desktop\face_recognition_system\images\face detector_2.jpg")
        img1=img1.resize((550,700),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=55,width=550,height=700)
        
        # 2nd img
        img2=Image.open(r"C:\Users\mramz\OneDrive\Desktop\face_recognition_system\images\facedetector22.webp")
        img2=img2.resize((750,600),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=550,y=55,width=750,height=600)
        
        # button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=280,y=528,width=180,height=35)
       
    #**************attendence***********************
    # def mark_attendance(self,i,r,n,d):
    #     with open("attendance.csv","r+",newline="\n")as f:
    #         myDataList=f.readlines()
    #         name_list=[]
    #         for line in myDataList:
    #             entry=line.split((","))
    #             name_list.append(entry[0])
    #         if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
    
    def mark_attendance_db(self,student_id, name, roll, dep):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password12",
                database="face_recognizer"
            )
            cursor = conn.cursor()

            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            cursor.execute("""
                INSERT INTO attendance 
                (student_id, roll, name, department, time, date, status)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """, (student_id, roll, name, dep, time, date, "Present"))

            conn.commit()

            print("Attendance marked")

        except mysql.connector.Error as err:
            if err.errno == 1062:
                pass
            else:
                print("Error:", err)

        finally:
            conn.close()
                      
                
            
    # *******************face recognition***********
        
    def face_recog(self):
            # 
            def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
                
                coord=[]
                
                for (x,y,w,h) in features:
                    # draw rectangle
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    # to predict image
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])     #width and height of rec
                    confidence=int((100*(1-predict/300)))               #formula
                    
                    # collecting data from mysql
                    conn=mysql.connector.connect(host="localhost",username="root",password="password12",database="face_recognizer")
                    my_cursor=conn.cursor()
                    
                    #data from sql
                    # my_cursor.execute("select Name from student where Student_id="+str(id))
                    # # fetching data
                    # n=my_cursor.fetchone()
                    # n="+".join(n)
                    
                    # my_cursor.execute("select Roll from student where Student_id="+str(id))
                    # r=my_cursor.fetchone()
                    # r="+".join(r)
                    
                    # my_cursor.execute("select Dep from student where Student_id="+str(id))
                    # d=my_cursor.fetchone()
                    # d="+".join(d)
                    
                    # my_cursor.execute("select Student_id from student where Student_id="+str(id))
                    # i=my_cursor.fetchone()
                    # i="+".join(i)
                    
                    my_cursor.execute(
                        "SELECT Student_id,Name, Roll, Dep FROM student WHERE Student_id=%s",(id,))
                    result = my_cursor.fetchone()

                    if result:
                        i, n, r, d = result
                        i = str(i)
                        n = str(n)
                        r = str(r)
                        d = str(d)
                    else:
                        i, n, r, d = "Unknown", "Unknown", "Unknown", "Unknown"
                        
                    conn.close()

                    # # -------- Name --------
                    # my_cursor.execute("select Name from student where Student_id=" + str(id))
                    # n = my_cursor.fetchone()
                    # if n is None:
                    #     n = "Unknown"
                    # else:
                    #     n = n[0]

                    # # -------- Roll --------
                    # my_cursor.execute("select Roll from student where Student_id=" + str(id))
                    # r = my_cursor.fetchone()
                    # if r is None:
                    #     r = "Unknown"
                    # else:
                    #     r = r[0]

                    # # -------- Department --------
                    # my_cursor.execute("select Dep from student where Student_id=" + str(id))
                    # d = my_cursor.fetchone()
                    # if d is None:
                    #     d = "Unknown"
                    # else:
                    #     d = d[0]

                    # # -------- Student ID --------
                    # my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                    # i = my_cursor.fetchone()
                    # if i is None:
                    #     i = "Unknown"
                    # else:
                    #     i = i[0]

                    # conn.close()
                    
                    
                    if confidence > 77:
                        cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendance_db(i,r,n,d)
                    else:               #for unknown face
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,h]
                    
                return coord
                       
            # don not repeat yourself
            def recognize(img,clf,faceCascade):
                coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
                return img
                
            faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
            
            video_cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
            
            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("welcome to face recognition",img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            video_cap.release()
            cv2.destroyAllWindows()
                
if __name__ == "__main__":      #
    root=Tk()                   #call root from toolkit
    obj=Face_Recognition(root, lambda: None)        #making classs object
    root.mainloop()