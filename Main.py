from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Student():
    def __init__(self,main):
        self.win = Tk()
        self.win.title("College Management System")
        self.win.config(bg='wheat')
        self.win.maxsize(width=800,height=700)
        self.win.minsize(width=800,height=600)

        # ============ Title Label =============
        title = Label(self.win,text="College Management System",bg='brown',relief=GROOVE,bd='10',fg='black',font=("Times new roman",35))
        title.pack(fill=BOTH,side=TOP)

        # =========== Log in Frame ============
        left_frame = Frame(self.win,bg='blue',bd='5',relief=RIDGE)
        left_frame.place(x=190,y=135,width=400,height=300)

        m_title = Label(left_frame,text=' Admin Login ',bg='cyan',font=('Times new roman',25))
        m_title.grid(row=0,column=0,padx=10,pady=10)
        # m_title.place(x=40,y=10)

        # Entry 
        uname=lbl_username = Label(left_frame,text='Username :',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_username.grid(row=1,column=0,padx=20,pady=20,sticky='w')

        self.uname = Entry(left_frame,relief=RIDGE,font=('Times new roman',15,'bold'))
        self.uname.grid(row=1,column=0,padx=170,pady=10)
        
        lbl_password = Label(left_frame,text='Password :',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_password.grid(row=2,column=0,padx=25,pady=10,sticky='w')

        self.upass = Entry(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'))
        self.upass.grid(row=2,column=0,padx=170,pady=10,sticky='w')

        # Button
        # btn = Button(left_frame,text='Login',font=('Times new roman',10,'bold'),bg='green',width='15',height='2',command=self.Dopen)
        btn = Button(left_frame,text='Login',font=('Times new roman',10,'bold'),bg='green',width='15',height='2',command=self.a1)
        # btn.grid(row=3,column=0,padx=10,pady=10)
        btn.place(x=190,y=210)

    def a1(self):
        conn=pymysql.connect(host="localhost",user="root",password="root",db="smpy")
        mycur=conn.cursor()
        sql="select * from login"
        mycur.execute(sql)
        result=mycur.fetchall()
        for x in result:
            em=x[0]
            pa=x[1]
            # print(em)
            # print(pa)
        user = self.uname.get() 
        password = self.upass.get()
        if (user == em and password == pa):
            self.Dopen()
        else:
            messagebox.showerror("Error",'''Username and password is wrong.\nPlease enter a valid username & password.''')

    def Dopen(self):
        self.main = Tk()
        self.main.config(bg='cyan')
        # self.main.iconbitmap("25Icon.ico")
        self.main.maxsize(width=1550,height=800)
        self.main.minsize(width=1450,height=800)
        self.main.title("College Management System")

        title = Label(self.main,text="College Management System",bg='brown',relief=GROOVE,bd='10',fg='black',font=("Times new roman",45))
        title.pack(fill=BOTH,side=TOP)

        # ========== All variables =========
        self.Roll_No_var = StringVar()
        self.first_name_var = StringVar()
        self.middle_name_var = StringVar()
        self.last_name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.course_var = StringVar()
        self.year_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        #=========== Left Frame ===========
        left_frame = Frame(self.main,bg='blue',bd='5',relief=RIDGE)
        left_frame.place(x=20,y=100,width=450,height=700)

        m_title = Label(left_frame,text='Manage Data',bg='yellow',font=('Times new roman',25))
        m_title.grid(row=0,columnspan=2,pady=10,padx=10)

        lbl_roll = Label(left_frame,text='Roll No',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_roll.grid(row=1,column=0,padx=10,pady=10,sticky='w')
        etn_roll = Entry(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'),textvariable=self.Roll_No_var)
        etn_roll.grid(row=1,column=2,padx=10,pady=10,sticky='w')

        lbl_first_name = Label(left_frame,text='First Name :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_first_name.grid(row=2,column=0,padx=10,pady=5,sticky='w')
        etn_first_name = Entry(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'),textvariable=self.first_name_var)
        etn_first_name.grid(row=2,column=2,padx=10,pady=5,sticky='w')

        lbl_middle_name = Label(left_frame,text='Middle Name :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_middle_name.grid(row=3,column=0,padx=10,pady=5,sticky='w')
        etn_middle_name = Entry(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'),textvariable=self.middle_name_var)
        etn_middle_name.grid(row=3,column=2,padx=10,pady=5,sticky='w')

        lbl_last_name = Label(left_frame,text='Last Name :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_last_name.grid(row=4,column=0,padx=10,pady=5,sticky='w')
        etn_last_name = Entry(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'),textvariable=self.last_name_var)
        etn_last_name.grid(row=4,column=2,padx=10,pady=5,sticky='w')

        lbl_email = Label(left_frame,text='Email :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_email.grid(row=5,column=0,padx=10,pady=5,sticky='w')
        etn_email = Entry(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'),textvariable=self.email_var)
        etn_email.grid(row=5,column=2,padx=10,pady=5,sticky='w')

        lbl_gender = Label(left_frame,text='Gender :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_gender.grid(row=6,column=0,padx=10,pady=5,sticky='w')
        combo_gender = ttk.Combobox(left_frame,font=('Times new roman',15,'bold'),state='readonly',width=18,textvariable=self.gender_var)
        combo_gender['values'] = ("Male","Female","Other")
        combo_gender.grid(row=6,column=2,padx=10,pady=5,sticky='w')

        lbl_Course = Label(left_frame,text='Course :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_Course.grid(row=7,column=0,padx=10,pady=5,sticky='w')
        combo_Course = ttk.Combobox(left_frame,font=('Times new roman',15,'bold'),state='readonly',width=18,textvariable=self.course_var)
        combo_Course['values'] = ("Infromation Technology","Computer Technology","Civil Engineering","Mechanical Engineering")
        combo_Course.grid(row=7,column=2,padx=10,pady=5,sticky='w')

        lbl_Year = Label(left_frame,text='Year :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_Year.grid(row=8,column=0,padx=10,pady=5,sticky='w')
        combo_Year = ttk.Combobox(left_frame,font=('Times new roman',15,'bold'),state='readonly',width=18,textvariable=self.year_var)
        combo_Year['values'] = ("First Year","Second Year","Third Year","Final Year")
        combo_Year.grid(row=8,column=2,padx=10,pady=5,sticky='w')

        lbl_contact = Label(left_frame,text='Contact :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_contact.grid(row=9,column=0,padx=10,pady=4,sticky='w')
        etn_contact = Entry(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'),textvariable=self.contact_var)
        etn_contact.grid(row=9,column=2,padx=10,pady=4,sticky='w')

        lbl_dob = Label(left_frame,text='D.B.O :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_dob.grid(row=10,column=0,padx=10,pady=5,sticky='w')
        etn_dob = Entry(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'),textvariable=self.dob_var)
        etn_dob.grid(row=10,column=2,padx=10,pady=5,sticky='w')

        lbl_Address = Label(left_frame,text='Address :-',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_Address.grid(row=11,column=0,padx=10,pady=5,sticky='w')
        self.txt_Address = Text(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'),width=20,height=3)
        # self.txt_Address = Entry(left_frame,relief=GROOVE,font=('Times new roman',15,'bold'))
        self.txt_Address.grid(row=11,column=2,padx=10,pady=5,sticky='w')

        #========== Button Frame =========
        btn_frame = Frame(self.main,bg='black',bd='4',relief=GROOVE)
        btn_frame.place(x=30,y=730,width=428)

        Addbtn = Button(btn_frame,text='Add',font=('Times new roman',10,'bold'),bg='cyan',width='11',command=self.add_students).grid(row=0,column=0,padx=8,pady=10)
        Updatebtn = Button(btn_frame,text='Update',font=('Times new roman',10,'bold'),bg='cyan',width='11',command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn = Button(btn_frame,text='Delete',font=('Times new roman',10,'bold'),bg='cyan',width='11',command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn = Button(btn_frame,text='Clear',font=('Times new roman',10,'bold'),bg='cyan',width='11',command=self.clear_data).grid(row=0,column=3,padx=10,pady=10)

        #========= Right Frame(Details Frame) ========
        right_frame = Frame(self.main,bg='blue',bd='5',relief=RIDGE)
        right_frame.place(x=500,y=100,width=1000,height=650)

        lbl_search = Label(right_frame,text='Search By',bg='blue',fg='white',font=('Times new roman',20,'bold'))
        lbl_search.grid(row=0,columnspan=2,padx=5,pady=10)

        combo_search = ttk.Combobox(right_frame,font=('Times new roman',15,'bold'),textvariable=self.search_by,state='readonly',width=25)
        combo_search['values'] = ('Roll_No','First_Name','Middle_Name','Last_Name','Gender','Course')
        combo_search.grid(row=0,column=2,padx=30,pady=5,sticky='w')

        ent_search = Entry(right_frame,bd=4,font=('Times new roman',15),textvariable=self.search_txt).grid(row=0,column=3,padx=20,pady=5,sticky='w')

        btn_search = Button(right_frame,text='Search',width=12,height=2,bg="green",fg='white',font=('arial',10,'bold'),command=self.search_data).grid(row=0,column=4,padx=20,pady=5,sticky='w')
        btn_show_all = Button(right_frame,text='Show All',width=12,height=2,bg="green",fg='white',font=('arial',10,'bold'),command=self.fetch_data).grid(row=0,column=5,padx=20,pady=1,sticky='w')

        #======= Table Frame =========
        tabel_frame = Frame(right_frame,bg='crimson',bd=4,relief=RIDGE)
        tabel_frame.place(x=25,y=100,width=940,height=500)

        scroll_x = Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(tabel_frame,orient=VERTICAL)

        self.Student_table = ttk.Treeview(tabel_frame,columns=("roll","first name","middle name","last name","email","gender","course","year","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("first name",text="First Name")
        self.Student_table.heading("middle name",text="Middle Name")
        self.Student_table.heading("last name",text="Last Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("year",text="Year")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")

        self.Student_table["show"]='headings'
        self.Student_table.column("roll",width=80)
        self.Student_table.column("first name",width=80)
        self.Student_table.column("middle name",width=80)
        self.Student_table.column("last name",width=80)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=80)
        self.Student_table.column("course",width=80)
        self.Student_table.column("year",width=80)
        self.Student_table.column("contact",width=80)
        self.Student_table.column("dob",width=80)
        self.Student_table.column("address",width=120)
                
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor) # Event generate
        self.fetch_data()

    def add_students(self):
        self.fetch_data()
        if self.Roll_No_var.get() == "" or self.first_name_var.get() == "" or self.middle_name_var.get() == "" or self.last_name_var.get() == "" or self.email_var.get() == "" or self.gender_var.get() == "" or self.course_var.get() == "" or self.year_var.get() == "" or self.contact_var.get() == "" or self.dob_var.get() == "" or self.txt_Address.get('1.0',END) == "":
            messagebox.showerror("Error","All fields are required to fill.")
        else:
            con = pymysql.connect(host="localhost",user="root",password="root",db="smpy")
            cur = con.cursor()
            # print("Connected")
            cur.execute("insert into stu_data values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                            self.first_name_var.get(),
                                                                                            self.middle_name_var.get(),
                                                                                            self.last_name_var.get(),
                                                                                            self.email_var.get(),
                                                                                            self.gender_var.get(),
                                                                                            self.course_var.get(),
                                                                                            self.year_var.get(),
                                                                                            self.contact_var.get(),
                                                                                            self.dob_var.get(),
                                                                                            self.txt_Address.get('1.0',END)))
            messagebox.showinfo("Success","Record has been inserted.")
            con.commit()
            con.close()
            self.fetch_data()
            self.clear_data()

    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",db="smpy")
        cur = con.cursor()
        cur.execute("select * from stu_data")
        rows = cur.fetchall()
        if len(rows)!= 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("",END,values=row)
        con.commit()
        con.close()
            
    def clear_data(self):
        self.Roll_No_var.set("")
        self.first_name_var.set("")
        self.middle_name_var.set("")
        self.last_name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.course_var.set("")
        self.year_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete('1.0',END)
        
    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.first_name_var.set(row[1])
        self.middle_name_var.set(row[2])
        self.last_name_var.set(row[3])
        self.email_var.set(row[4])
        self.gender_var.set(row[5])
        self.course_var.set(row[6])
        self.year_var.set(row[7])
        self.contact_var.set(row[8])
        self.dob_var.set(row[9])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[10])

    def update_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",db="smpy")
        cur = con.cursor()
        cur.execute("update stu_data set first_name=%s, middle_name=%s, last_name=%s, email=%s, gender=%s, course=%s, year=%s, contact=%s, dob=%s, address=%s where roll_no=%s ",(

                                                                                                self.first_name_var.get(),
                                                                                                self.middle_name_var.get(),
                                                                                                self.last_name_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.gender_var.get(),
                                                                                                self.course_var.get(),
                                                                                                self.year_var.get(),
                                                                                                self.contact_var.get(),
                                                                                                self.dob_var.get(),
                                                                                                self.txt_Address.get('1.0',END),
                                                                                                self.Roll_No_var.get()))
        messagebox.showinfo("Success","Record has been inserted.")
        con.commit()
        con.close()
        self.fetch_data()
        self.clear_data()
            
    def delete_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",db="smpy")
        cur = con.cursor()
        cur.execute("delete from stu_data where roll_no=%s", self.Roll_No_var.get())
        messagebox.showinfo("Success","Selected data has been deleted successfully.")
        con.commit()
        con.close()
        self.fetch_data()
        self.clear_data()

    def search_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",db="smpy")
        cur = con.cursor()
        cur.execute("select * from stu_data where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!= 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
        # self.fetch_data()
        # self.clear_data()

class Student():
    pass
    main = Tk()
    obj = Student(main)
    main.mainloop()