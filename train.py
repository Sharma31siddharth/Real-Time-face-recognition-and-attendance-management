from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x770+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=45)

        img_top=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\download.jpg")
        img_top=img_top.resize((1430,275),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1430,height=275)

        #button
        b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=0,y=300,width=1430,height=60)

        img_bottom=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\gr.jpg")
        img_bottom=img_bottom.resize((1430,275),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=360,width=1430,height=275)

    def train_classifier(self):
        data_dir=("DATA")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training ",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed")

        
            
        





        
        


         









        

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        
