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

        # Product Search Fram=============================
        productframe2=Frame(productframe1,bd=2,relief=RIDGE,bg="white")
        productframe2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(productframe2,text="Serch Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        lbl_search=Label(productframe2,text="Product Name",font=("times new roman",15,"bold"),bg="white",fg="Black").place(x=2,y=45)
        txt_search=Entry(productframe2,textvariable=self.var_Search,font=("times new roman",15),bg="lightyellow").place(x=130,y=47,width=150,height=25)
        btn_search=Button(productframe2,text="Serach",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=290,y=45,width=100,height=25)
        btn_show_all=Button(productframe2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=290,y=10,width=100,height=25)

        # Product Detail Fram=============================
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
        
        ## Customer Fram =======
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        customerframe=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        customerframe.place(x=420,y=110,width=530,height=70)

        ctital=Label(customerframe,text="Customer Detail",font=("goudy old style",15,),bg="lightgray" ).pack(side=TOP,fill=X)
        lbl_name=Label(customerframe,text="Name",font=("times new roman",15,),bg="white",fg="Black").place(x=5,y=35)
        txt_name=Entry(customerframe,textvariable=self.var_cname,font=("times new roman",15),bg="lightyellow").place(x=80,y=35,width=150,height=25)

        lbl_contact=Label(customerframe,text="Contact No",font=("times new roman",15,),bg="white",fg="Black").place(x=250,y=35)
        txt_contact=Entry(customerframe,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=350,y=35,width=150,height=25)

        ### Cal Card Fram =====================
        cal_card_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        cal_card_frame.place(x=420,y=190,width=530,height=360)

        ### Calculator Fram =====================
        self.var_cal_input=StringVar()
        
        cal_frame=Frame(cal_card_frame,bd=9,relief=RIDGE,bg="white")
        cal_frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(cal_frame,textvariable=self.var_cal_input,font=("arial",15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly')
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(cal_frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(cal_frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(cal_frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(cal_frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(cal_frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(cal_frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(cal_frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(cal_frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=3)

        btn_1=Button(cal_frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(cal_frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(cal_frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(cal_frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(cal_frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=11,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(cal_frame,text='C',font=('arial',15,'bold'),bd=5,width=4,pady=11,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(cal_frame,text='=',font=('arial',15,'bold'),bd=5,width=4,pady=11,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(cal_frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=11,cursor="hand2").grid(row=4,column=3)

        ### Card Fram =====================
        card_frame=Frame(cal_card_frame,bd=3,relief=RIDGE,bg="white")
        card_frame.place(x=280,y=8,width=245,height=342)
        cardtital=Label(card_frame,text="Card \t Total Product : [0]",font=("goudy old style",15,),bg="lightgray" ).pack(side=TOP,fill=X)



        Scrolly=Scrollbar(card_frame,orient=VERTICAL)
        Scrollx=Scrollbar(card_frame,orient=HORIZONTAL)

        self.cardtable=ttk.Treeview(card_frame,columns=("pid","name","price","qty","status"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.cardtable.xview)
        Scrolly.config(command=self.cardtable.yview)
        self.cardtable.heading("pid",text="PID")
        self.cardtable.heading("name",text="Supplier Name")
        self.cardtable.heading("price",text="Price")
        self.cardtable.heading("qty",text="QTY")
        self.cardtable.heading("status",text="Status")
        self.cardtable["show"]="headings" 
        self.cardtable.column("pid",width=40)
        self.cardtable.column("name",width=100)
        self.cardtable.column("price",width=90)
        self.cardtable.column("qty",width=40)
        self.cardtable.column("status",width=90)
        self.cardtable.pack(fill=BOTH,expand=1)
        #self.cardtable.bind("<ButtonRelease-1>",self.get_data)

        ### ADD Card Widgets Button =====================  
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_prices=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        add_cardwidgetsframe=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        add_cardwidgetsframe.place(x=420,y=550,width=530,height=110)

        lbl_name=Label(add_cardwidgetsframe,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_name=Entry(add_cardwidgetsframe,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_prices=Label(add_cardwidgetsframe,text="Prices Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_prices=Entry(add_cardwidgetsframe,textvariable=self.var_prices,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(add_cardwidgetsframe,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(add_cardwidgetsframe,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_Instock=Label(add_cardwidgetsframe,text="In Stock[9999]",font=("times new roman",15),bg="white")
        self.lbl_Instock.place(x=5,y=70)

        btn_clear_card=Button(add_cardwidgetsframe,text="Clear",font=("times new roman",15),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_card=Button(add_cardwidgetsframe,text="Add | Update card",font=("times new roman",15),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        



# =================== All Function ==========================================
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)



if __name__=="__main__":         
    root=Tk()
    obj=BillClass(root)
    root.mainloop()