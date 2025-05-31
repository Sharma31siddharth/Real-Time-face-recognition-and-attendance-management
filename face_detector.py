from tkinter import *
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
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x770+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1430,height=45)

        img2=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\ai.webp")
        img2=img2.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=55,width=650,height=700)

        img3=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\App-with-face-recognition.jpg")
        img3=img3.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=640,y=55,width=950,height=700)

        #button

        b1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_rec,font=("times new roman",15,"bold"),bg="darkgreen",fg="white")
        b1.place(x=370,y=500,width=200,height=40)

        #attendance
    def mark_attendance(self,s,r,n,d):
        with open("siddharth.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((s not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%Y-%m-%d")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{r},{n},{d},{dtString},{d1},present")

            






                
            
            


        #face recognition

    def face_rec(self):
            
            def draw_boundray(img,classifier,scaleFactor,minNegihbors,color,text,clf):

                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNegihbors)

                coord=[]
                
                for(x,y,w,h) in features:
                    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    conn=mysql.connector.connect(host="localhost",username="root",password="$iddh@rtH2004",database="facerecognition")
                    my_cursor=conn.cursor()

                    my_cursor.execute("SELECT Name FROM student WHERE studentid=%s", (str(id),))
                    n = my_cursor.fetchone()
                    n = "+".join(n) if n is not None else "Unknown"

                    my_cursor.execute("SELECT Roll FROM student WHERE studentid=%s", (str(id),))
                    r = my_cursor.fetchone()
                    r = "+".join(r) if r is not None else "Unknown"

                    my_cursor.execute("SELECT Dep FROM student WHERE studentid=%s", (str(id),))
                    d = my_cursor.fetchone()
                    d = "+".join(d) if d is not None else "Unknown"

                    my_cursor.execute("SELECT studentid FROM student WHERE studentid=%s", (str(id),))
                    s = my_cursor.fetchone()
                    s = "+".join(s) if s is not None else "Unknown"


                    if confidence > 77:
                        cv2.putText(img,f"ID:{s}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendance(s,r,n,d)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,h]
                return coord

            def recognize(img,clf,faceCascade):
                coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
                return img


            faceCascade=cv2.CascadeClassifier(r"C:\Users\siddharth sharma\AppData\Roaming\Python\Python311\site-packages\cv2\data\haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap=cv2.VideoCapture(0)

            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome To Face Recognition",img)

                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()
                    
                        


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop() 
