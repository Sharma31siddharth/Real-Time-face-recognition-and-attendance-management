from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x770+0+0")
        self.root.title("Attendance")

        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1430,height=45)

        img1=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\laptop-1209008_960_720.webp")
        img1=img1.resize((1400,640),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=55,width=1400,height=640)

        
        dev_label=Label(f_lbl,text="Email: sharma31siddharth@gamil.com",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=450,y=200)





if __name__=="__main__":
    root=Tk()
    obj=Help( root)
    root.mainloop() 
