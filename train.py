from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import messagebox              #to show message
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root, back_callback):
        self.root=root  
        self.back_callback = back_callback #initialize root
        self.root.geometry("1530x790+0+0")        #geometry of lap. resolution,x,y
        self.root.title("face Recognition System")
        
        # get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        title_label=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),fg="white",bg="#4a4a4a")
        title_label.place(x=0,y=0,width=screen_width,height=50)
        
        back_btn = Button(self.root,
                  text="← Back",
                  command=self.back_callback,
                  font=("times new roman", 12, "bold"),
                  bg="#4a4a4a",
                  fg="white")

        back_btn.place(x=10, y=10)   
        
        # img_top=Image.open(r"C:\Users\mramz\OneDrive\Desktop\face_recognition_system\images\student_img.png")
        # img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=55,width=1530,height=325)
        
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="#4a4a4a",fg="white")
        b1_1.place(x=500,y=280,width=300,height=100)
        
        
        # img_bottom=Image.open(r"C:\Users\mramz\OneDrive\Desktop\face_recognition_system\images\student_img.png")
        # img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        # f_lbl=Label(self.root,image=self.photoimg_bottom)
        # f_lbl.place(x=0,y=440,width=1530,height=325)
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]  
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #gray scale img
            imageNP=np.array(img,'uint8')  #unit8 datatype
            id=int(os.path.split(image)[1].split('.')[1]) 
            
            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)
       # =============== Train The Classifier And Save ============
        clf=cv2.face.LBPHFaceRecognizer_create()    
        clf.train(faces,ids)
        clf.write("classifier.xml") 
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
        
if __name__ == "__main__":      
    root=Tk()                   
    obj=Train(root)       
    root.mainloop()