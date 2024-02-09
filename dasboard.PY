from tkinter import*
from PIL import Image,ImageTk     #== pip install pillow ====
from employee import employeeClass
from supplier import supplierclass
from category import categoryclass
from product import productClass
from Sales import salesclass
class IMS:
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

        #=== Left Menu ===
        self.menuLogo=Image.open("images/menu_im.png")
        self.menuLogo=self.menuLogo.resize((200,200))
        self.menuLogo=ImageTk.PhotoImage(self.menuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white") 
        LeftMenu.place(x=0,y=105,width=200,height=565) 

        lbl_menuLogo=Label(LeftMenu,image=self.menuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("time new roman",20,"bold"),bg="#009688").pack(side=TOP,fill=X)
        
        btn_Employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",18,"bold"),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",18,"bold"),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",18,"bold"),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",18,"bold"),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",18,"bold"),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",18,"bold"),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #=== Conttent ===
        self.lbl_employee=Label(self.root,text="Total Employee\n [ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style,",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_Supplier=Label(self.root,text="Total Supplier\n [ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style,",20,"bold"))
        self.lbl_Supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_Cataegory=Label(self.root,text="Total Cataegory\n [ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style,",20,"bold"))
        self.lbl_Cataegory.place(x=1000,y=120,height=150,width=300)

        self.lbl_Product=Label(self.root,text="Total Product\n [ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style,",20,"bold"))
        self.lbl_Product.place(x=300,y=300,height=150,width=300)

        self.lbl_Sales=Label(self.root,text="Total Sales\n [ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style,",20,"bold"))
        self.lbl_Sales.place(x=650,y=300,height=150,width=300)  
        
        #=== Footer ===
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Devlaoped By Mishra Enterprises\n for Any Technical issue Contact : 9096536487",font=("times new roman",15,),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
#===================================================================================      

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesclass(self.new_win)
        
if __name__=="__main__":         
    root=Tk()
    obj=IMS(root)
    root.mainloop()