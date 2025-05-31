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

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x770+0+0")
        self.root.title("Attendance")
        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        

        img=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\student.jpg")
        img=img.resize((650,180),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=650,height=180)

        
        img1=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\download.jpg")
        img1=img1.resize((650,180),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=0,width=650,height=180)

         #bg image
        img3=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\ai.webp")
        img3=img3.resize((1430,690),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg2)
        bg_img.place(x=0,y=110,width=1430,height=690)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=10,width=1430,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=4,y=55,width=1260,height=500)

        Left_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_Frame.place(x=4,y=10,width=620,height=510)

        img_left=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\Student-Attendance-Automation-1024x538.png")
        img_left=img_left.resize((610,110),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_Frame,image=self.photoimg_left)
        f_lbl.place(x=4,y=0,width=610,height=110)

        left_inside_frame=Frame(Left_Frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=4,y=115,width=610,height=370)

        #labels and entry
        #attendance id

        attendanceid_label=Label(left_inside_frame,text="ATTENDANCE_ID",font=("times new roman",10,"bold"))
        attendanceid_label.grid(row=0,column=0,padx=10,sticky=W)

        attendanceid_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",10,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,sticky=W)

        #roll
        
        roll_label=Label(left_inside_frame,text="ROLL:",font=("comicsansns",10,"bold"))
        roll_label.grid(row=0,column=2,padx=4,pady=8)

        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("comicsansns",10,"bold"))
        roll_entry.grid(row=0,column=3,pady=8)

        #name

        name_label=Label(left_inside_frame,text="NAME",font=("comicsansns",10,"bold"))
        name_label.grid(row=1,column=0)

        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("comicsansns",10,"bold"))
        name_entry.grid(row=1,column=1,pady=8)

        #department

        dep_label=Label(left_inside_frame,text="DEPARTMENT",font=("comicsansns",10,"bold"))
        dep_label.grid(row=1,column=2)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("comicsansns",10,"bold"))
        dep_entry.grid(row=1,column=3,pady=8)

        #time
        time_label=Label(left_inside_frame,text="TIME",font=("comicsansns",10,"bold"))
        time_label.grid(row=2,column=0)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("comicsansns",10,"bold"))
        time_entry.grid(row=2,column=1,pady=8)

        #date
        date_label=Label(left_inside_frame,text="DATE",font=("comicsansns",10,"bold"))
        date_label.grid(row=2,column=2)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("comicsansns",10,"bold"))
        date_entry.grid(row=2,column=3,pady=8)

        #attendance

        attendanceLabel=Label(left_inside_frame,text="ATTENDANCE STATUS",font="comicansans 10 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 10 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=280,width=700,height=35)

        #import
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=27,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #export
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=27,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #update
        #delete_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        #delete_btn.grid(row=0,column=2)

        #reset
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=27,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        #right frame

        Right_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_Frame.place(x=630,y=10,width=620,height=500)

        table_frame=Frame(Right_Frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=600,height=400)

        #scroll bar table

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL FILE","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL FILE","*.*")),parent=self.root)
            with open(fln,mode="w",newline="")as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                 messagebox.showerror("error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
  
       
        

        
            




if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop() 
