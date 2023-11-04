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

        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)

        #===== Tital =======
        tit=Label(product_frame,text="Manage Product Details",font=("goudy old style",18,"bold",),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        lal_category=Label(product_frame,text="Category",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=60)
        lal_supplier=Label(product_frame,text="Supplier",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=110)
        lal_product_name=Label(product_frame,text="Name",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=160)
        lal_price=Label(product_frame,text="Price",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=210)
        lal_qty=Label(product_frame,text="Quantity",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=260)
        lal_status=Label(product_frame,text="Status",font=("goudy old style",18,"bold",),bg="white").place(x=30,y=310)




if __name__=="__main__":         
    root=Tk()
    obj=productClass(root)
    root.mainloop()