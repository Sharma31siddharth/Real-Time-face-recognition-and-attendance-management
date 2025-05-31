from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from train import Train
from face_detector import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime




class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x770+0+0")
        self.root.title("face recognition system")

        img=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\images.jpg")
        img=img.resize((640,110),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=640,height=110)

        
        img1=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\download.jpg")
        img1=img1.resize((640,110),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=640,y=0,width=640,height=110)


        #img2 = Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\images.jpg")
        #img2=img2.resize((450,110),Image.Resampling.LANCZOS)
        #self.photoimg2=ImageTk.PhotoImage(img2)

        #f_lbl=Label(self.root,image=self.photoimg2)
        #f_lbl.place(x=900,y=0,width=450,height=110)

        #bg image
        img3=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\ai.webp")
        img3=img3.resize((1430,710),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg2)
        bg_img.place(x=0,y=110,width=1430,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=45)

        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student button
        img4=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\student.jpg")
        img4=img4.resize((220,100),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1_1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1_1.place(x=100,y=50,width=200,height=200)

        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=100,y=220,width=200,height=30)

        img5=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\face.jpeg")
        img5=img5.resize((220,100),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=400,y=50,width=200,height=200)

        b2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=400,y=220,width=200,height=30)

        img6=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\attendance.png")
        img6=img6.resize((220,100),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=700,y=50,width=200,height=200)

        b3=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3.place(x=700,y=220,width=200,height=30)

        img7=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\help.png")
        img7=img7.resize((220,100),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1000,y=50,width=200,height=200)

        b4=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4.place(x=1000,y=220,width=200,height=30)

        img8=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\traindata.webp")
        img8=img8.resize((220,100),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=100,y=300,width=200,height=200)

        b5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5.place(x=100,y=500,width=200,height=30)

        img9=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\gr.jpg")
        img9=img9.resize((220,100),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b6.place(x=400,y=300,width=200,height=200)

        b6=Button(bg_img,text="Photo",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6.place(x=400,y=500,width=200,height=30)

        img10=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\developer.jpg")
        img10=img10.resize((220,100),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=700,y=300,width=200,height=200)

        b7=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7.place(x=700,y=500,width=200,height=30)

        img11=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\Glass_exit_sign.jpg")
        img11=img11.resize((220,100),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b7.place(x=1000,y=300,width=200,height=200)

        b7=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7.place(x=1000,y=500,width=200,height=30)
        
    def open_image(self):
        os.startfile("DATA")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


    #Function buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

 





        




        

        

        
        











if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()
