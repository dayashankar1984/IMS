from tkinter import*
from PIL import Image,ImageTk     #== pip install pillow ====
from tkinter import ttk,messagebox
import sqlite3

class supplierclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x600+220+130")
        self.root.title("Inventory Managment System | Developed By Daya")
        self.root.config(bg="white",)
        #root.resizable(False,False)
        self.root.focus_force()
        
        #==========================
        # All variables
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()
                
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        

        #==== Searchfram ===
        searchfram=LabelFrame(self.root,text="Search Employee",font=("goudy old style,",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchfram.place(x=250,y=20,width=600,height=70)
        
        #==== Options =======
        cmb_search=ttk.Combobox(searchfram,textvariable=self.var_searchBy,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("gudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchfram,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="light yellow").place(x=200,y=12)
        btn_search=Button(searchfram,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #===== Tital =======
        tit=Label(self.root,text="Supplier Details",font=("goudy old style",15,"bold",),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)


        #======== Content ========
        #====== Row1 ========

        lal_supplier_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=150,)   
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=150,y=150,width=180)
    

        #===== Row2 ======
        lal_name=Label(self.root,text="Supplier Name",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=190,)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=150,y=190,width=180)
        
        #===== Row3 ======
        lal_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=230,)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=150,y=230,width=180)
        
        #===== Row4 ======
        lal_desc=Label(self.root,text="Description",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=270,)
        self.txt_desc=Text(self.root,font=("goudy old style",15,"bold",),bg="Lightyellow")
        self.txt_desc.place(x=150,y=270,width=300,height=60)

        #====== buttons =======
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.Delete,font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

        #====== Emplyee Details ===========

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=250) # fram Size

        Scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        Scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.suppliertable=ttk.Treeview(emp_frame,columns=("Invoice","name","contact","desc"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.suppliertable.xview)
        Scrolly.config(command=self.suppliertable.yview)

        self.suppliertable.heading("Invoice",text="Invoice No")
        self.suppliertable.heading("name",text="Supplier Name")
        self.suppliertable.heading("contact",text="Contact No")
        self.suppliertable.heading("desc",text="Depcription")
        
        self.suppliertable["show"]="headings" 

        self.suppliertable.column("Invoice",width=90)
        self.suppliertable.column("name",width=100)
        self.suppliertable.column("contact",width=100)
        self.suppliertable.column("desc",width=100)
        
        self.suppliertable.pack(fill=BOTH,expand=1)
        self.suppliertable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#======================================================================================================================

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error","Employee ID Must be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error","this Employee id already assigned, try different",parent=self.root)
                else:
                    cur.execute("insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                self.var_sup_invoice.get(),
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),

                                                self.var_dob.get(),
                                                self.var_doj.get(),

                                                self.var_pass.get(),
                                                self.var_utype.get(),
                                                self.txt_desc.get('1.0',END),
                                                self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Addedd Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                                                                                           
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.suppliertable.delete(*self.suppliertable.get_children())
            for row in rows:
                self.suppliertable.insert('',END,values=row)

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.suppliertable.focus()
        content=(self.suppliertable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])

        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[9]),
        self.var_salary.set(row[10])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error","Employee ID Must be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                                
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),
                                                self.var_pass.get(),
                                                self.var_utype.get(),
                                                self.txt_desc.get('1.0',END),
                                                self.var_salary.get(),
                                                self.var_sup_invoice.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def Delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error","Employee ID Must be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("Delete from employee where eid=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        self.show()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")

        self.var_dob.set("")
        self.var_doj.set("")

        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_desc.delete('1.0',END),
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchBy.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchBy.get()=="Select":
                messagebox.showerror("Error","Select search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)

            else:
                cur.execute("select * from employee where "+self.var_searchBy.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.suppliertable.delete(*self.suppliertable.get_children())
                    for row in rows:
                        self.suppliertable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found !!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

        
if __name__=="__main__":         
    root=Tk()
    obj=supplierclass(root)
    root.mainloop()