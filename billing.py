from tkinter import*
from PIL import Image,ImageTk     #== pip install pillow ====
from tkinter import ttk,messagebox
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title(" Inventory Managment System | Developed By Dayashankar Mishra ")
        self.root.config(bg="white")
        #=== title ===
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Managment System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #=== btn_logout ===
        btn_logout=Button(self.root,text="Logout",font=("time new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #=== clock ===
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Managment System\t\t Date: DD-MM-YYYY\t\t Time : HH:MM:SS",font=("times new roman",15,),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        # Product Fram =============
        self.var_Search=StringVar()
        
        productframe1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        productframe1.place(x=6,y=110,width=410,height=550)

        Ptital=Label(productframe1,text="All Product",font=("goudy old style",20,),bg="#262626",fg="white").pack(side=TOP,fill=X)

        productframe2=Frame(productframe1,bd=2,relief=RIDGE,bg="white")
        productframe2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(productframe2,text="Serch Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        lbl_search=Label(productframe2,text="Product Name",font=("times new roman",15,"bold"),bg="white",fg="Black").place(x=2,y=45)
        txt_search=Entry(productframe2,textvariable=self.var_Search,font=("times new roman",15),bg="lightyellow").place(x=130,y=47,width=150,height=25)
        btn_search=Button(productframe2,text="Serach",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=290,y=45,width=100,height=25)
        btn_show_all=Button(productframe2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=290,y=10,width=100,height=25)

        ProductFrame3=Frame(productframe1,bd=3,relief=RIDGE,bg="white")
        ProductFrame3.place(x=2,y=140,width=398,height=375) # fram Size

        Scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        Scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.product_Table.xview)
        Scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Supplier Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")
        self.product_Table["show"]="headings" 

        self.product_Table.column("pid",width=90)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        #self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(productframe1,text="Note: 'Enter 0 Qunatity to remove product from the card'",font=("goudy old style",12),anchor="w",bg="white",fg="red").pack(side=BOTTOM,fill=X)
        


if __name__=="__main__":         
    root=Tk()
    obj=BillClass(root)
    root.mainloop()