from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkcalendar import DateEntry


class Student :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x770+0+0")
        self.root.title("face recognition system")

        #variables
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

        img=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\images (1).jpg")
        img=img.resize((640,110),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=640,height=110)

        
        img1=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\download.jpg")
        img1=img1.resize((640,110),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=640,y=0,width=640,height=110)


        #img2=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\adgips.jpg")
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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1430,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=4,y=55,width=1260,height=500)

        #left label frame
        Left_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_Frame.place(x=4,y=10,width=620,height=500)

        img_left=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\images (2).jpg")
        img_left=img_left.resize((620,110),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_Frame,image=self.photoimg_left)
        f_lbl.place(x=4,y=0,width=620,height=110)
        
        #current course information
        
        current_course_Frame=LabelFrame(Left_Frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_Frame.place(x=4,y=115,width=620,height=130)
        #DEPARTMENT
        dep_label=Label(current_course_Frame,text="DEPARTMENT",font=("times new roman",10,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly")
        dep_combo["values"]=("select departement","computer","IT","civil","AI&DS","AI&ML")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_Frame,text="COURSE",font=("times new roman",10,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly")
        course_combo["values"]=("select Course","MSC","BSC","MTech","BTech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #YEAR
        year_label=Label(current_course_Frame,text="YEAR",font=("times new roman",10,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly")
        year_combo["values"]=("Year","2020-22","2020-23","2020-24","2021-25","2022-2026")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #SEMESTER
        semester_label=Label(current_course_Frame,text="SEMESTER",font=("times new roman",10,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","sem-1","sem-2","sem-3","sem-4","sem-5","sem-6","sem-7","sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        #class student info
        class_student_Frame=LabelFrame(Left_Frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_Frame.place(x=4,y=215,width=620,height=300)

        #STUDENTID
        studentid_label=Label(class_student_Frame,text="STUDENT_ID",font=("times new roman",10,"bold"))
        studentid_label.grid(row=0,column=0,padx=10,sticky=W)

        studentid_entry=ttk.Entry(class_student_Frame,textvariable=self.var_std_id,width=20,font=("times new roman",10,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,sticky=W)

         #STUDENTNAE
        studentname_label=Label(class_student_Frame,text="STUDENT_NAME",font=("times new roman",10,"bold"))
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_Frame,textvariable=self.var_std_name,width=20,font=("times new roman",10,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

          #CLASS DIVISION
        studentdiv_label=Label(class_student_Frame,text="CLASS_DIVISION",font=("times new roman",10,"bold"))
        studentdiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #studentdiv_entry=ttk.Entry(class_student_Frame,textvariable=self.var_div,width=20,font=("times new roman",10,"bold"))
        #studentdiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_Frame,textvariable=self.var_div,font=("times new roman",10,"bold"),state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

         #ROLLNO
        studentno_label=Label(class_student_Frame,text="ROLL_NO",font=("times new roman",10,"bold"))
        studentno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentno_entry=ttk.Entry(class_student_Frame,textvariable=self.var_roll,width=20,font=("times new roman",10,"bold"))
        studentno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #GENDER
        gender_label=Label(class_student_Frame,text="GENDER",font=("times new roman",10,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        gender_combo=ttk.Combobox(class_student_Frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        

         #DOB
        #studentdob_label=Label(class_student_Frame,text="DOB",font=("times new roman",10,"bold"))
        #studentdob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        #studentdob_entry=ttk.Entry(class_student_Frame,textvariable=self.var_dob,width=20,font=("times new roman",10,"bold"))
        #studentdob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        studentdob_label = Label(class_student_Frame, text="DOB", font=("times new roman", 10, "bold"))
        studentdob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        studentdob_entry = DateEntry(class_student_Frame, textvariable=self.var_dob, width=8,
                             font=("times new roman", 8, "bold"), background="darkblue", foreground="white", borderwidth=1)
        studentdob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)


         #EMAIL
        studentemail_label=Label(class_student_Frame,text="EMAIL:",font=("times new roman",10,"bold"))
        studentemail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentemail_entry=ttk.Entry(class_student_Frame,textvariable=self.var_email,width=20,font=("times new roman",10,"bold"))
        studentemail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         #PHONENO
        phone_label=Label(class_student_Frame,text="CONTACT NO.",font=("times new roman",10,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_Frame,textvariable=self.var_phone,width=20,font=("times new roman",10,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_Frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=4,column=0)
        
        
        radiobtn2=ttk.Radiobutton(class_student_Frame,variable=self.var_radio1,text="No photo sample",value="NO")
        radiobtn2.grid(row=4,column=1)

        #buttons frame
        btn_frame=Frame(class_student_Frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=145,width=700,height=35)

        #save button
        save_btn=Button(btn_frame,text="save",command=self.add_data,width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #update
        update_btn=Button(btn_frame,text="update",command=self.update_data,width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #delete
        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        #reset
        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_student_Frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=180,width=700,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=43,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=43,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)
        
        #right frame
        Right_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_Frame.place(x=630,y=10,width=620,height=500)

        img_right=Image.open(r"C:\Users\siddharth sharma\Desktop\face recognition system\f_images\student.jpg")
        img_right=img_right.resize((720,110),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_Frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=120)

        #=====search system======

        search_student_Frame=LabelFrame(Right_Frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_student_Frame.place(x=4,y=120,width=620,height=70)

        #search_label=Label(search_student_Frame,text="Search By",font=("times new roman",10,"bold"))
        #search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #search_combo=ttk.Combobox(search_student_Frame,font=("times new roman",10,"bold"),state="readonly")
        #search_combo["values"]=("Select","Roll_No","Phone_No")
        #search_combo.current(0)
        #search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #search_entry=ttk.Entry(search_student_Frame,width=18,font=("times new roman",10,"bold"))
        #search_entry.grid(row=0,column=2,padx=10,sticky=W)

        #search_btn=Button(search_student_Frame,text="search",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        #search_btn.grid(row=0,column=3,padx=4)

        #show_btn=Button(search_student_Frame,text="ShowAll",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        #show_btn.grid(row=0,column=4,padx=4)
        #table frame
        table_frame1=Frame(Right_Frame,bd=2,relief=RIDGE,bg="white")
        table_frame1.place(x=4,y=180,width=615,height=250)

        scroll_x=ttk.Scrollbar(table_frame1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame1,orient=VERTICAL)

        self.student_table = ttk.Treeview(
        table_frame1,
        columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="RollNo.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #=====function decration========
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_id.get()=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
            
        
        else:
            try:
                 conn=mysql.connector.connect(host="localhost",username="root",password="$iddh@rtH2004",database="facerecognition")
                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
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
                                                                                                self.var_phone.get()
                                                                                                
                                                                                                
                                                                                                     ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("success","student details has been added successfully",parent=self.root)
            except Exception as es:
                 messagebox.showerror("error",f"Due to :{str(es)}",parent=self.root)
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="$iddh@rtH2004",database="facerecognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()#data called 
        conn.close()


    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

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
        self.var_phone.set(data[11])

    #update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="$iddh@rtH2004",
                        database="facerecognition"
                )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                    "UPDATE student SET Dep=%s, Course=%s, Year=%s, semester=%s, Name=%s, Division=%s, Roll=%s,Gender=%s, Dob=%s, Email=%s, Phone=%s WHERE studentid=%s",
                    (
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
                        self.var_std_id.get()
                    )
                )
                
                else:
                    if not update:
                        return

                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
                
            except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



    #delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="$iddh@rtH2004",
                        database="facerecognition"
                        )
                    my_cursor = conn.cursor()
                    sql="delete from student where studentid=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully delete student details",parent= self.root)
                    
            except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")


    #generate data set take a photo sample
    def generate_dataset(self):
         if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            
         else:
            try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="$iddh@rtH2004",
                        database="facerecognition"
                )
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    my_cursor.execute(
                        "UPDATE student SET Dep=%s, Course=%s, Year=%s, semester=%s, Name=%s, Division=%s, Roll=%s,Gender=%s, Dob=%s, Email=%s, Phone=%s WHERE studentid=%s",
                    (
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
                        self.var_std_id.get()==id+1
                    )
                )
                    
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
    #load predifined data on face
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        #minimum neighbour=5

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1

                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="DATA/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("cropped face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets complites!!")
                    
            except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    
     






















                        
                        












                        
            
       





                
        

        

        
        
        

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()        

       
