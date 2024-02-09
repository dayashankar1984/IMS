from tkinter import*
from PIL import Image,ImageTk     #== pip install pillow ====
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x600+220+130")
        self.root.title("Inventory Managment System | Developed By Daya")
        self.root.config(bg="white",)
        #root.resizable(False,False)
        self.root.focus_force()
        #==========================
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_Pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()      

        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)

        #===== Tital =======
        tit=Label(product_frame,text="Manage Product Details",font=("goudy old style",18,"bold",),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        
        #==== column1 =======
        lal_category=Label(product_frame,text="Category",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=60)
        lal_supplier=Label(product_frame,text="Supplier",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=110)
        lal_product_name=Label(product_frame,text="Name",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=160)
        lal_price=Label(product_frame,text="Price",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=210)
        lal_qty=Label(product_frame,text="Quantity",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=260)
        lal_status=Label(product_frame,text="Status",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=310)
        #==== column2 =======
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("gudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("gudy old style",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_frame,textvariable=self.var_name,font=("gudy old style",15),bg="lightyellow").place(x=150,y=160,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("gudy old style",15),bg="lightyellow").place(x=150,y=210,width=200)
        txt_qty=Entry(product_frame,textvariable=self.var_qty,font=("gudy old style",15),bg="lightyellow").place(x=150,y=260,width=200)
        
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("gudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

        #====== buttons =======
        btn_add=Button(product_frame,text="Save",command=self.add,font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_frame,text="Delete",command=self.Delete,font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)

        #==== Searchfram ===
        searchfram=LabelFrame(self.root,text="Search Employee",font=("goudy old style,",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchfram.place(x=480,y=10,width=600,height=80)
        
        #==== Options =======
        cmb_search=ttk.Combobox(searchfram,textvariable=self.var_searchBy,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("gudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchfram,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="light yellow").place(x=200,y=12)
        btn_search=Button(searchfram,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #====== Product Details ===========

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390) # fram Size

        Scrolly=Scrollbar(p_frame,orient=VERTICAL)
        Scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("Pid","Category","Supplier","Name","Price","Qty","Status"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.product_table.xview)
        Scrolly.config(command=self.product_table.yview)


        self.product_table.heading("Pid",text="P ID")
        self.product_table.heading("Category",text="Category")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("Name",text="Name")
        self.product_table.heading("Price",text="Price")
        self.product_table.heading("Qty",text="Qty")
        self.product_table.heading("Status",text="Status")
       
        self.product_table["show"]="headings" 

        self.product_table.column("Pid",width=90)
        self.product_table.column("Category",width=100)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("Name",width=100)
        self.product_table.column("Price",width=100)
        self.product_table.column("Qty",width=100)
        self.product_table.column("Status",width=100)
        
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#============ Drop Down List in Catgarey and Supplier ===================
    def fetch_cat_sup(self): 
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])           
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
    
    #==== Add Function ========
        
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_sup.get()=="Select" or self.var_name.get()=="":
               messagebox.showerror("Error","All Fields are Required",parent=self.root)
            else:
                cur.execute("Select * from Product where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error","Product already Present, try different",parent=self.root)
                else:
                    cur.execute("insert into Product (Category,Supplier,Name,Price,Qty,Status) values(?,?,?,?,?,?)",(
                                                self.var_cat.get(),
                                                self.var_sup.get(),
                                                self.var_name.get(),
                                                self.var_price.get(),
                                                self.var_qty.get(),
                                                self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Addedd Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                                                                                           
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from Product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_Pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
        
        
        

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_Pid.get()=="":
               messagebox.showerror("Error","Please select product from list",parent=self.root)
            else:
                cur.execute("Select * from Product where Pid=?",(self.var_Pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Product ID",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,Name=?,Price=?,Qty=?,Status=? where Pid=?",(
                                                
                                                self.var_cat.get(),
                                                self.var_sup.get(),
                                                self.var_name.get(),
                                                self.var_price.get(),
                                                self.var_qty.get(),
                                                self.var_status.get(),
                                                self.var_Pid.get()

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
            if self.var_Pid.get()=="":
               messagebox.showerror("Error","Select Product from list",parent=self.root)
            else:
                cur.execute("Select * from Product where Pid=?",(self.var_Pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("Delete from Product where Pid=?",(self.var_Pid.get(),))
                        con.commit()
                        self.show()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_Pid.set("")
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
                cur.execute("select * from Product where "+self.var_searchBy.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found !!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)






if __name__=="__main__":         
    root=Tk()
    obj=productClass(root)
    root.mainloop()