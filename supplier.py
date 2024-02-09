from tkinter import*
from PIL import Image,ImageTk     #== pip install pillow ====
from tkinter import ttk,messagebox
import sqlite3

class supplierclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x600+220+130")
        self.root.title("Inventory Managment System | Developed By Daya")
        self.root.config(bg="white")
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
        #==== Options =======
        lbl_search=Label(self.root,text="Invoice No.",bg="white",font=("gudy old style",15))
        lbl_search.place(x=700,y=80)

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="light yellow").place(x=800,y=80,width=143,height=30)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=950,y=79,width=100,height=30)

        #===== Tital =======
        tit=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold",),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)

        #======== Content ========
        #====== Row1 ========

        lal_supplier_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=80,)   
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=180,y=80,width=180)
    
        #===== Row2 ======
        lal_name=Label(self.root,text="Name",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=120,)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=180,y=120,width=180)
        
        #===== Row3 ======
        lal_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=160,)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=180,y=160,width=180)
        
        #===== Row4 ======
        lal_desc=Label(self.root,text="Description",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=200,)
        self.txt_desc=Text(self.root,font=("goudy old style",15,"bold",),bg="Lightyellow")
        self.txt_desc.place(x=180,y=200,width=470,height=120)

        #====== buttons =======
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.Delete,font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)

        #====== Supplier Details ===========

        emp_frame=Frame(self.root,bd=3,relief=RIDGE,bg="blue")
        emp_frame.place(x=700,y=150,width=350,height=350) # fram Size

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
               messagebox.showerror("Error","Invoice must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error","this invoice no. already assigned, try different",parent=self.root)
                else:
                    cur.execute("insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                                self.var_sup_invoice.get(),
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier Addedd Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)                                                                              
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
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
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[3]),

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error","Invoice no. Must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Invoice No",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                                
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_desc.get('1.0',END),
                                                self.var_sup_invoice.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def Delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error","Invoice no. must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Invoice No",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("Delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        self.show()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END),
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)

            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.suppliertable.delete(*self.suppliertable.get_children())
                    self.suppliertable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found !!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

        
if __name__=="__main__":         
    root=Tk()
    obj=supplierclass(root)
    root.mainloop()