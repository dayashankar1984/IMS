from tkinter import*
#from PIL import Image,ImageTk     #== pip install pillow ====
from tkinter import ttk,messagebox
import sqlite3

class bankclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x768+0+0")
        self.root.title("Inventory Managment System | Developed By Daya")
        self.root.config(bg="white",)
        #root.resizable(False,False)
        self.root.focus_force()
        
        #==========================
        # All variables
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()
                
        self.var_acc_no=StringVar()
        self.var_name=StringVar()
        self.var_fname=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()

        self.var_vill=StringVar()
        self.var_post=StringVar()
        self.var_distt=StringVar()
        self.var_pin=StringVar()
        self.var_mobile=StringVar()

        self.var_pancard=StringVar()
        self.var_c_i_f=StringVar()
        self.var_addhar=StringVar()       
        self.var_A_type=StringVar()
        


    

        #==== Searchfram ===
        searchfram=LabelFrame(self.root,text="Search Account",font=("goudy old style,",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchfram.place(x=350,y=20,width=600,height=70)
        
        #==== Options =======
        cmb_search=ttk.Combobox(searchfram,textvariable=self.var_searchBy,values=("Select","Account No","Mobile No","Account No"),state='readonly',justify=CENTER,font=("gudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchfram,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="light yellow").place(x=200,y=12)
        btn_search=Button(searchfram,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #===== Tital =======
        tit=Label(self.root,text="Bank Detail",font=("goudy old style",15,"bold",),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1180)


        #======== Content ========
        #====== Lable ========

        lal_acc=Label(self.root,text="Account No",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=150,)
        lal_name=Label(self.root,text="Name",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=200,)
        lal_f_name=Label(self.root,text="Father Name",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=250,)
        lal_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=300,)
        lal_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold",),bg="white").place(x=50,y=350,)
     
        lal_vill=Label(self.root,text="Vill",font=("goudy old style",15,"bold",),bg="white").place(x=370,y=150,)
        lal_post=Label(self.root,text="Post",font=("goudy old style",15,"bold",),bg="white").place(x=370,y=200,)
        lal_distt=Label(self.root,text="Distt",font=("goudy old style",15,"bold",),bg="white").place(x=370,y=250,)
        lal_pin=Label(self.root,text="Pin Code",font=("goudy old style",15,"bold",),bg="white").place(x=370,y=300,)
        lal_mobno=Label(self.root,text="Mobile No",font=("goudy old style",15,"bold",),bg="white").place(x=370,y=350,)
        
        lal_pan=Label(self.root,text="Pan Card",font=("goudy old style",15,"bold",),bg="white").place(x=700,y=150,)
        lal_cif=Label(self.root,text="C.I.F",font=("goudy old style",15,"bold",),bg="white").place(x=700,y=200,)
        lal_addhar=Label(self.root,text="Addhar No",font=("goudy old style",15,"bold",),bg="white").place(x=700,y=250,)
        lal_atype=Label(self.root,text="A/C Type",font=("goudy old style",15,"bold",),bg="white").place(x=700,y=300,)
        
        #===== Entry ======
   
        txt_acc=Entry(self.root,textvariable=self.var_acc_no,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=170,y=150,width=180)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=170,y=200,width=180)
        txt_f_name=Entry(self.root,textvariable=self.var_fname,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=170,y=250,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=170,y=300,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("gudy old style",15,))
        cmb_gender.place(x=170,y=350,width=180)
        cmb_gender.current(0)
        
        txt_vill=Entry(self.root,textvariable=self.var_vill,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=490,y=150,width=180)
        txt_post=Entry(self.root,textvariable=self.var_post,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=490,y=200,width=180)
        txt_distt=Entry(self.root,textvariable=self.var_distt,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=490,y=250,width=180)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=490,y=300,width=180)
        txt_mobno=Entry(self.root,textvariable=self.var_mobile,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=490,y=350,width=180)

        txt_pan=Entry(self.root,textvariable=self.var_pancard,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=830,y=150,width=180)
        txt_cif=Entry(self.root,textvariable=self.var_c_i_f,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=830,y=200,width=180)
        txt_=Entry(self.root,textvariable=self.var_addhar,font=("goudy old style",15,"bold",),bg="Lightyellow").place(x=830,y=250,width=180)
        cmb_atype=ttk.Combobox(self.root,textvariable=self.var_A_type,values=("Saving","Other"),state='readonly',justify=CENTER,font=("gudy old style",15,))
        cmb_atype.place(x=830,y=300,width=180)
        cmb_atype.current(0)
        
        #====== buttons =======
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=700,y=350,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=820,y=350,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.Delete,font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=940,y=350,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=1060,y=350,width=110,height=28)

        #====== Bank Detail Fram ===========

        bank_frame=Frame(self.root,bd=3,relief=RIDGE)
        bank_frame.place(x=0,y=400,relwidth=1,height=250) # fram Size

        Scrolly=Scrollbar(bank_frame,orient=VERTICAL)
        Scrollx=Scrollbar(bank_frame,orient=HORIZONTAL)

        self.Banktable=ttk.Treeview(bank_frame,columns=("aid","name","fname","dob","gender","vill","post","distt","pin","mobile","pan","cif","addhar","atype"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.Banktable.xview)
        Scrolly.config(command=self.Banktable.yview)


        self.Banktable.heading("aid",text="Account No")
        self.Banktable.heading("name",text="Name")
        self.Banktable.heading("fname",text="Father Name")
        self.Banktable.heading("dob",text="D.O.B")
        self.Banktable.heading("gender",text="Gender")
        self.Banktable.heading("vill",text="Vill")
        self.Banktable.heading("post",text="Post")
        self.Banktable.heading("distt",text="Distt")
        self.Banktable.heading("pin",text="Pin")
        self.Banktable.heading("mobile",text="Mobile No")
        self.Banktable.heading("pan",text="Pan Card")
        self.Banktable.heading("cif",text="C.I.F")
        self.Banktable.heading("addhar",text="Addhar No")
        self.Banktable.heading("atype",text="A Type")
        self.Banktable["show"]="headings" 

        self.Banktable.column("aid",width=90)
        self.Banktable.column("name",width=25)
        self.Banktable.column("fname",width=25)
        self.Banktable.column("dob",width=15)
        self.Banktable.column("gender",width=15)
        self.Banktable.column("vill",width=100)
        self.Banktable.column("post",width=100)
        self.Banktable.column("distt",width=100)
        self.Banktable.column("pin",width=7)
        self.Banktable.column("mobile",width=100)
        self.Banktable.column("pan",width=10)
        self.Banktable.column("cif",width=15)
        self.Banktable.column("addhar",width=15)
        self.Banktable.column("atype",width=15)

        self.Banktable.pack(fill=BOTH,expand=1)
        self.Banktable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    #============ Save Data Funcation =================

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_acc_no.get()=="":
               messagebox.showerror("Error","Account No Must be Required",parent=self.root)
            else:
                cur.execute("Select * from bank where aid=?",(self.var_acc_no.get(),))
                row=cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error","this Account No already assigned, try different",parent=self.root)
                else:
                    cur.execute("insert into bank (aid,name,fname,dob,gender,vill,post,distt,pin,mobile,pan,cif,addhar,atype) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                                                self.var_acc_no.get(),
                                                self.var_name.get(),
                                                self.var_fname.get(),
                                                self.var_dob.get(),
                                                self.var_gender.get(),
                                                self.var_vill.get(),
                                                self.var_post.get(),
                                                self.var_distt.get(),
                                                self.var_pin.get(),
                                                self.var_mobile.get(),
                                                self.var_pancard.get(),
                                                self.var_c_i_f.get(),
                                                self.var_addhar.get(),
                                                self.var_A_type.get(),
                                                
                                                
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Account Addedd Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    # Show Function used in data show in fram ========

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from bank")
            rows=cur.fetchall()
            self.Banktable.delete(*self.Banktable.get_children())
            for row in rows:
                self.Banktable.insert('',END,values=row)

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    #======= Get Function ============

    def get_data(self,ev):
        f=self.Banktable.focus()
        content=(self.Banktable.item(f))
        row=content['values']
        #print(row)
        self.var_acc_no.set(row[0])
        self.var_name.set(row[1])
        self.var_fname.set(row[2])
        self.var_dob.set(row[3])
        self.var_gender.set(row[4])
        self.var_vill.set(row[5])
        self.var_post.set(row[6])
        self.var_distt.set(row[7])
        self.var_pin.set(row[8])
        self.var_mobile.set(row[9])
        self.var_pancard.set(row[10])
        self.var_c_i_f.set(row[11])
        self.var_addhar.set(row[12])
        self.var_A_type.set(row[13])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_acc_no.get()=="":
               messagebox.showerror("Error","Account No Must be Required",parent=self.root)
            else:
                cur.execute("Select * from bank where aid=?",(self.var_acc_no.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Account No",parent=self.root)
                else:
                    cur.execute("Update bank set name=?,fname=?,dob=?,gender=?,vill=?,post=?,distt=?,pin=?,mobile=?,pan=?,cif=?,addhar=?,atype=? where aid=?",(
                                                
                                                self.var_name.get(),
                                                self.var_fname.get(),
                                                self.var_dob.get(),
                                                self.var_gender.get(),
                                                self.var_vill.get(),
                                                self.var_post.get(),
                                                self.var_distt.get(),
                                                self.var_pin.get(),
                                                self.var_mobile.get(),
                                                self.var_pancard.get(),
                                                self.var_c_i_f.get(),
                                                self.var_addhar.get(),
                                                self.var_A_type.get(),
                                                self.var_acc_no.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Account Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    



    def Delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_acc_no.get()=="":
               messagebox.showerror("Error","Account No Must be Required",parent=self.root)
            else:
                cur.execute("Select * from bank where aid=?",(self.var_acc_no.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Account No",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("Delete from bank where aid=?",(self.var_acc_no.get(),))
                        con.commit()
                        self.show()
                        messagebox.showinfo("Delete","Account Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def clear(self):
        self.var_acc_no.set("")
        self.var_name.set("")
        self.var_fname.set("")
        self.var_dob.set("")
        self.var_gender.set("Select")
        self.var_vill.set("")
        self.var_post.set("")
        self.var_distt.set("")
        self.var_pin.set("")
        self.var_mobile.set("")
        self.var_pancard.set("")
        self.var_c_i_f.set("")
        self.var_addhar.set("")
        self.var_A_type.set("Select")
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
                cur.execute("select * from Bank where "+self.var_searchBy.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Banktable.delete(*self.Banktable.get_children())
                    for row in rows:
                        self.Banktable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found !!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#======================================================================================================================

        
if __name__=="__main__":         
    root=Tk()
    obj=bankclass(root)
    root.mainloop()