from tkinter import*
from PIL import Image,ImageTk     #== pip install pillow ====
from tkinter import ttk,messagebox
import sqlite3
import os
class salesclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x600+220+130")
        self.root.title("Inventory Managment System | Developed By Daya")
        self.root.config(bg="white",)
        #root.resizable(False,False)
        self.root.focus_force()

        self.bill_list=[]
        self.Var_invoice=StringVar()

    #===== TITAL ==========
        lbl_tital=Label(self.root,text="View Customer Bills",font=("goudy old style",30,"bold"),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_invoice=Label(self.root,text="Invoice No",font=("times new roman",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.Var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)
    
        btn_search=Button(self.root,text="Search",command=self.Search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgray",fg="black",cursor="hand2").place(x=490,y=100,width=120,height=28)
        # Bill List Area==============
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)

        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)

        # Custmorer Bill Area =======

        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=330)

        lbl_tital2=Label(bill_frame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="orange").pack(side=TOP,fill=X)
        
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,font=("goudy old style",15),bg="lightpink",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        #==== Image ========
        self.bill_photo=Image.open("images/cat2.jpg")
        self.bill_photo=self.bill_photo.resize((450,300))
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=700,y=110)

        self.show()
################################################################
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        #print(os.listdir('../IMS'))
        for i in os.listdir('bill'):
            #print(i.split('.'),i.split('.')[-1])
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()          

    def Search(self):
        if self.Var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no should be required",parent=self.root)
        else:
            if self.Var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.Var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No",parent=self.root)


    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)




if __name__=="__main__":         
    root=Tk()
    obj=salesclass(root)
    root.mainloop()