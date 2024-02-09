import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)") 
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)") 
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)") 
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(Pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,Name text,Price text,Qty text,Status text)") 
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Bank(aid INTEGER PRIMARY KEY AUTOINCREMENT,name text,fname text,dob text,gender text,vill text,post text,distt text,pin text,mobile text,pan text,cif text,addhar text,atype text)") 
    con.commit()

create_db()