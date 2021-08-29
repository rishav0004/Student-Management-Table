from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import cx_Oracle

# window = tk.Tk()
# g = tk.Label(text="Student Management Table",font = ("",40,"bold"),foreground = "orange",background = "black")
# f = tk.Label(text="next label")
# window.title('MAIN')
# window.geometry("1000x500")
# g.grid(row = 0,column =0,sticky = 'EW')
# g.pack(side=TOP, fill=X)

# b = Button(text="click onn")
# b.pack()
# f.pack()

# window.mainloop()

class student:
    def __init__(self,root):
        self.root = root
        self.root.title("MANAGEMENT TABLE")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root,text="Student Management Table",font =("trbuchet ms",40,"bold") ,bg = "orange",fg ="black")
        title.pack(side=TOP,fill = X)

        self.roll_no_var = StringVar()
        self.name_var =  StringVar()
        self.contact_var =  StringVar()
        self.gender_var =  StringVar()
        self.email_var =  StringVar()
        self.address_var =  StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt_variable = StringVar()
        # input()

        # add students
        def add_students():              
                con = cx_Oracle.connect("test1/mahajan@localhost")
                cur = con.cursor()
                #cur.execute("insert into students (roll_no,name,email,gender,contact,dob,address)" "values (self.roll_no_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get())")
                try:
                        cur.execute("""insert into students (roll_no, name, email,gender,contact,dob,address) values (:1,:2,:3,:4,:5,:6,:7)""",(self.roll_no_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END)))
                        # print(self.roll_no_var.get())
                        con.commit()
                # except unique constraint (TEST1.STUDENTS_CON) violated:
                #         onclick("Roll no is reserved")
                #onclick("data added ")
                        clear_all()                        
                        display_all()
                        con.close()
                        messagebox.showinfo("showinfo", "Data added")
                        # self.student_table.column("roll",width = "90",values = "")             
                        pass
                except cx_Oracle.IntegrityError:
                        messagebox.showerror("ERROR","Error occured during adding data")
                        pass
                except cx_Oracle.DatabaseError:
                        messagebox.showerror("ERROR","Enter specific datatype")
#DatabaseError
# ORA-01722: invalid number
                        

                ##unique constraint (TEST1.STUDENTS_CON) violated
                # cx_Oracle.IntegrityError: ORA-00001: unique constraint (TEST1.STUDENTS_CON) violated

        
        def display_all():
                con = cx_Oracle.connect("test1/mahajan@localhost")
                cur = con.cursor()
                
                sql = """select * from students order by roll_no"""
                cur.execute(sql)
                row = cur.fetchall()
                
                if len(row)>0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in row:
                                self.student_table.insert("",END,values = i)
                        
                        con.commit()
                con.close()

        def search_by_txt():
                con = cx_Oracle.connect("test1/mahajan@localhost")
                cur = con.cursor()
                
                cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+self.search_txt_variable.get()+"%'")
                print(self.search_by.get())
                print(self.search_txt_variable.get())
                # +str(self.search_by.get())+" like '% "+str(self.search_txt.get())+"%'")
                # select * from students where contact LIKE '%00%'

                data = cur.fetchall()

                # print(data)
                # if len(row)>0:
                self.student_table.delete(*self.student_table.get_children())
                print(data)
                con.commit()

                # tree.delete(*tree.get_children())
                
                # for i in row:
                #         self.student_table.insert("",END,values = i)
                # for i in data:
                #         # self.student_table.insert(" ",END,values = i)
                #         print(i)
                
                # for i in data:
                #        self.student_table.insert("",END,values = i)
                        
                        # con.commit()
                con.close()


                
        def clear_all():
                self.roll_no_var.set("")
                self.name_var.set("")
                self.email_var.set("")
                self.gender_var.set("")
                self.contact_var.set("")
                self.dob_var.set("")
                self.txt_address.delete('1.0',END)
                # self.student_table.column(*tree,"")
        
        def delete_data():
                con = cx_Oracle.connect("test1/mahajan@localhost")
                cur = con.cursor()
                cur.execute("""delete from students where roll_no = :1 and name = :2""",(self.roll_no_var.get(),self.name_var.get()))

                con.commit()

                display_all()
                clear_all()
                self.student_table.column("roll",width = "90",values = "")             

                
        def Update_data():
                con = cx_Oracle.connect("test1/mahajan@localhost")
                cur = con.cursor()
                #cur.execute("insert into students (roll_no,name,email,gender,contact,dob,address)" "values (self.roll_no_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get())")
                
                
                        # cur.execute("""update students (roll_no, name, email,gender,contact,dob,address) values (:1,:2,:3,:4,:5,:6,:7)""",(self.roll_no_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END)))
                cur.execute("""update students set roll_no = :1, 
                                                        name =:2,
                                                        email =:3,
                                                        gender =:4,
                                                        contact =:5,
                                                        dob =:6,
                                                        address =:7 where roll_no = :8""",(self.roll_no_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END),self.roll_no_var.get()))
                con.commit()
                display_all()
                clear_all()
                self.student_table.column("roll",width = "90",values = "")             

                # except unique constraint (TEST1.STUDENTS_CON) violated:
                #         onclick("Roll no is reserved")
                #onclick("data added ")
                        
                con.close()
                
        

        def get_cursor(event):


                # if not self.student_table.selection():
                #         print("ERROR: NOT SELECTED")
                #         messagebox.showwarning("Error", "Item Not Selected!")
                # else:


                

                curItem = self.student_table.focus()
                contents = (self.student_table.item(curItem))
                selectedItem = contents["values"]
                                
                # print(selectedItem)
                self.roll_no_var.set(selectedItem[0])
                self.name_var.set(selectedItem[1])
                self.email_var.set(selectedItem[2])
                self.gender_var.set(selectedItem[3])
                self.contact_var.set(selectedItem[4])
                self.dob_var.set(selectedItem[5])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,selectedItem[6])
                                        
                # self.student_table.column("roll",width = "90")
                # self.student_table.column("name",width = "140")
                # self.student_table.column("email",width = "140")
                # self.student_table.column("gender",width = "140")
                # self.student_table.column("contact",width = "140")
                # self.student_table.column("dob",width = "140")
                # self.student_table.column("address",width = "140")
                # con = cx_Oracle.connect("test1/mahajan@localhost")
                # cur = con.cursor()
                # sql = """select * from students where roll_no = %s"""
                # cur.execute(sql)
                # rows = cur.fetchall()
        
        # def table_click():
        #                 get_cursor()
                

                
# =============================LEFT SIDE=======================
        
        left_frame = Frame(self.root,bd = 4,relief = RIDGE,bg  = "orange")
        left_frame.place(x=20,y=80,width =550,height = 610)
        left_frame_title = Label(left_frame,text = "Enter Details",bg = 'orange',font = ("trbuchet ms",30,"bold"),fg = 'white')
        left_frame_title.grid(row = 0,columnspan = 2,pady =20,padx =120)

                            # =========rollno==========

        left_frame_rollno = Label(left_frame,text = "Roll Number",bg = 'orange',font = ("trbuchet ms",13,"bold"),fg = 'white')
        left_frame_rollno.grid(row = 1,pady =20,padx = 10,sticky = 'w')
        txt_rollno = Entry(left_frame,textvariable = self.roll_no_var,font = ("trbuchet ms",15,"bold"),bd = 5,relief = GROOVE)
        txt_rollno.grid(row =1,column = 1,padx = 50)
                            # =========name==========

        left_frame_name  = Label(left_frame,text = "Name",bg = 'orange',font = ("trbuchet ms",13,"bold"),fg = 'white')
        left_frame_name.grid(row = 2,pady =10,padx = 10,sticky = 'w')
        txt_name = Entry(left_frame,textvariable = self.name_var,font = ("trbuchet ms",15,"bold"),bd = 5,relief = GROOVE)
        txt_name.grid(row = 2,column = 1,padx = 50)
                        
                        # =========phoneno==========

        left_frame_phoneno = Label(left_frame,text = "Contact Number",bg = 'orange',font = ("trbuchet ms",13,"bold"),fg = 'white')
        left_frame_phoneno.grid(row = 3,pady =15,padx = 10,sticky = 'w')
        txt_phoneno = Entry(left_frame,textvariable = self.contact_var,font = ("trbuchet ms",15,"bold"),bd = 5,relief = GROOVE)
        txt_phoneno.grid(row =3,column = 1,padx = 50)
                           
                        # =========email==========


        left_frame_email = Label(left_frame,text = "Email",bg = 'orange',font = ("trbuchet ms",13,"bold"),fg = 'white')
        left_frame_email.grid(row = 4,pady =15,padx = 10,sticky = 'w')
        txt_email = Entry(left_frame,textvariable = self.email_var,font = ("trbuchet ms",15,"bold"),bd = 5,relief = GROOVE)
        txt_email.grid(row = 4,column = 1,padx = 50)

        left_frame_gender = Label(left_frame,text = "Gender",bg = 'orange',font = ("trbuchet ms",13,"bold"),fg = 'white')
        left_frame_gender.grid(row = 5,pady =15,padx = 10,sticky = 'w')
        drowpdown_gender = ttk.Combobox(left_frame,textvariable = self.gender_var,font = ("trbuchet ms",18,"bold"),width = 16,state = "readonly")
        drowpdown_gender["values"] = ("male","female",'other')
        drowpdown_gender.grid(row = 5,column = 1,padx = 10)

                                        
                        # =========DOB==========

        left_frame_DOB = Label(left_frame,text ="DOB",bg = 'orange',font = ("trbuchet ms",13,"bold"),fg = 'white')
        left_frame_DOB.grid(row = 6,pady =15,padx = 10,sticky = 'w')
        txt_DOB = Entry(left_frame,textvariable = self.dob_var,font = ("trbuchet ms",15,"bold"),bd = 5,relief = GROOVE)
        txt_DOB.grid(row =6,column = 1,padx = 50)

                        # =========Address==========
        
        left_frame_address = Label(left_frame,text = "Address",bg = 'orange',font = ("trbuchet ms",13,"bold"),fg = 'white')
        left_frame_address.grid(row = 7,pady =15,padx = 10,sticky = 'w')
        txt_address = Entry(left_frame,textvariable = self.address_var,font = ("trbuchet ms",15,"bold"),bd = 5,relief = GROOVE)
        self.txt_address = Text(left_frame,height = 5,width = 28)
        self.txt_address.grid(row =7,column = 1,padx = 50,pady = 10)

                        # =========left_Buttons==========
        button_frame = Frame(left_frame,bd = 4,relief = RIDGE,bg = 'orange')
        button_frame.place(x = 10,y = 540,width = 500)

        add_button = Button(button_frame,text = "Add",font = ("trbuchet ms",12,"bold"),width = 8,command = lambda:add_students()).grid(row = 0,column = 0,pady = 5,padx = 17)
        delete_button = Button(button_frame,text = "Delete",font = ("trbuchet ms",12,"bold"),width = 8,command = lambda:delete_data()).grid(row = 0,column = 1,pady = 5,padx = 17)
        update_button = Button(button_frame,text = "Update",font = ("trbuchet ms",12,"bold"),width = 8,command = lambda:Update_data()).grid(row = 0,column = 2,pady = 5,padx = 17)
        clear_button = Button(button_frame,text = "Clear",font = ("trbuchet ms",12,"bold"),width = 8,command = lambda:clear_all()).grid(row = 0,column = 3,pady = 5,padx = 17)

# 

        


                # ==========================RIGHT SIDE=======================


        right_frame = Frame(self.root,bd = 4,relief = RIDGE,bg  = "orange" )
        right_frame.place(x=580,y=80,width =760,height = 610)

                # ============================search by=======================

        right_search_by = Label(right_frame,text = "Search By :",bg = 'orange',font = ("trbuchet ms",18,"bold"),fg = 'white')
        right_search_by.grid(row = 0,column =0,pady =15,padx = 10)
        right_search_by_dropdown = ttk.Combobox(right_frame,textvariable = self.search_by,font = ("trbuchet ms",15,"bold"),width = 10,state = "readonly")
        right_search_by_dropdown["values"] = ("roll_no","name",'contact')
        right_search_by_dropdown.grid(row = 0,column = 1,padx = 10)

        right_txt_search=Entry(right_frame,textvariable = self.search_txt_variable,font = ("trbuchet ms",15,"bold"),bd = 5,relief = GROOVE)

        right_txt_search = Text(right_frame,height = 1.6,width = 18)
        right_txt_search.grid(row =0,column = 2,padx = 30,pady = 20)

        # right_search_by_button = Frame(right_frame,bd = 4,relief = RIDGE,bg = 'orange')
        # right_search_by_button.place(x = 500,y = 15,width = 250)

        right_search_button = Button(right_frame,text = "Search",font = ("trbuchet ms",12,"bold"),width = 8,command =lambda:search_by_txt()).grid(row = 0,column = 3,pady = 2,padx = 10)
        right_showall_button = Button(right_frame,text = "ShowAll",font = ("trbuchet ms",12,"bold"),width = 8,command =lambda:display_all()).grid(row = 0,column = 4,pady = 2,padx = 17)

                        # ============TABLE FRAME=================

        table_frame = Frame(self.root,bd = 4,relief = RIDGE,bg ='white')          
        table_frame.place(x = 600,y = 160,width = 719,height = 500)

        scroll_x = Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient = VERTICAL)
        self.student_table = ttk.Treeview(table_frame,columns = ("roll","name","email","gender","contact","dob","address"),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_x.config(command= self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)
        self.student_table.heading("roll",text = "ROLL NO.")
        self.student_table.heading("name",text = "NAME")
        self.student_table.heading("email",text = "EMAIL ID")
        self.student_table.heading("gender",text = "GENDER")
        self.student_table.heading("contact",text = "CONTACT")
        self.student_table.heading("dob",text = "DATE OF BIRTH")
        self.student_table.heading("address",text = "ADDRESS")

        self.student_table['show'] = "headings"

        self.student_table.column("roll",width = "90")
        self.student_table.column("name",width = "140")
        self.student_table.column("email",width = "140")
        self.student_table.column("gender",width = "140")
        self.student_table.column("contact",width = "140")
        self.student_table.column("dob",width = "140")
        self.student_table.column("address",width = "140")
        
        self.student_table.bind("<Double-Button-1>",get_cursor)
        # self.student_table.bind_all(get_cursor)
        # get_cursor()

        # get_cursor()


        display_all()
        self.student_table.pack(fill=BOTH,expand=1)


        
         


root = Tk()
ob = student(root)
root.mainloop()

# class main:
#     def __init__(self,root):
#         self.root = root
#         self.root.title("MAIN PROGRAM")
#         self.root.geometry()
#         # self.root.geometry("1350x700+0+0")
#         # title = Label(self.root,text="Student Management Table",font =("segoe script",40,"bold") ,bg = "yellow",fg ="red")
#         self.pack()
#         # title.pack(side=TOP,fill=X)

# root = Tk()
# ob = main(root)
# root.mainloop()
