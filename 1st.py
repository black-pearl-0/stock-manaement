from tkinter import *


from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

import sqlite3  as db
from PIL import Image
import mysql.connector

import os
 
# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("New Account")
    register_screen.geometry("1920x1080")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
     
    Label(register_screen, text="Enter details below", bg="Yellow").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="New Account", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1920x1080")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry

 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
     
    connn=mysql.connector.connect(host="localhost",user="root",database="21cs022",port=3306)
    print(con)
    currr=connn.cursor()

    #Insert
    insert="insert into re(user,pass) values (%s,%s)"
    user=(username_info,password_info)
    currr.execute(insert,user)
    connn.commit()
    print("Data Inserted")
    

    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    userpass=[]
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    conn=mysql.connector.connect(host="localhost",user="root",database="21cs022",port=3306)
    sel="select *from re where user ='%s' and pass='%s'"%(username1,password1)
    curr=conn.cursor()

    try :
     curr.execute(sel)
     res=curr.fetchall()
     for row in res :
        for x in row :
            userpass.append(x)
    except :
       print("Error")
       
    if (username1 and password1) in userpass :
        print("Login Successfull")
        login_sucess()
    elif username1 not in userpass :
        user_not_found()
        exit
    elif password1 not in userpass :
        password_not_recognised()
        exit    

        
        
        
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("1920x1080")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    
    
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("1920x1080")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("1920x1080")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 

    

 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 

# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    global x
    main_screen = Tk()
   
    main_screen.geometry("1920x1080")
    main_screen.title("Account Login")
    Label(text="Stock Maintanence System", bg="#ff4d4d",fg="white", width="300", height="2", font=("times", 30)).pack()
    
    Label(text="",bg="#d1d8e0").pack()
    main_screen.config(bg="#d1d8e0")
    Button(text="Login", height="2", width="30",font=("times",14), command = login,activebackground="#20bf6b").pack()
    Label(text="",bg="#d1d8e0").pack()
    Button(text="Register", height="2",font=("times",14),  width="30", command=register).pack()
    










def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()
    def connection():
     
     
      connectObj = db.connect("shopManagement.db")
      cur = connectObj.cursor()
      sql ='''create table if not exists sellings (date string,product string,price number,quantity number,total number)'''
      cur.execute(sql)
      connectObj.commit()
      
    connection()
    window=Tk()
    window.title("Stock Management")
    window.geometry("1920x1080")

    tabs = ttk.Notebook(window)
 
    root= ttk.Frame(tabs)
    root2=ttk.Frame(tabs)

    tabs.add(root, text ='Sell') 
    tabs.add(root2, text ='Stock')
    tabs.pack(expand = 1, fill ="both") 
  

#----------------------------------------------tab1 ----------------------------------
    def GenerateBill():
      connectObj = db.connect("shopManagement.db")
      cur = connectObj.cursor()  

      global billarea
      if p1quantity.get()==0 and p2quantity.get()==0 and p3quantity.get()==0 and p4quantity.get()==0:
        messagebox.showerror("Error","No product purchased")
      else:
        billarea.delete('1.0',END)
        billarea.insert(END,"\t|| Shop Management ||")
        billarea.insert(END,"\n_________________________________________\n")
        billarea.insert(END,"\nDate\t Products\tPrice\t   QTY\t Total")  
        billarea.insert(END,"\n==========================================")

        price= IntVar()
        price2=IntVar()
        price3=IntVar()
        price4=IntVar()

        print(dateE.get())
        price=price2=price3=price4=0

        if p1quantity.get()!=0:
            price=p1quantity.get()*p1price.get()
            print(price)
            billarea.insert(END,f"\n{dateE.get()}\t Product-1 \t{p1price.get()}\t {p1quantity.get()}\t {price}")

            sql = '''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Product-1',p1price.get(),p1quantity.get(),price))
            connectObj.commit() 

        if p2quantity.get()!=0:
            price2=(p2quantity.get()*p2price.get())
            print(price2)
            billarea.insert(END,f"\n{dateE.get()}\t Product-2 \t{p2price.get()}\t {p2quantity.get()}\t {price2}")

            sql = '''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            print(dateE.get(),'Product-2',p2price.get(),p2quantity.get(),price2)
            cur.execute(sql,(dateE.get(),'Product-2',p2price.get(),p2quantity.get(),price2))
            connectObj.commit() 

        if p3quantity.get()!=0:
            price3=p3quantity.get()*p1price.get()
            print(price3)
            billarea.insert(END,f"\n{dateE.get()}\tProduct-3 \t{p3price.get()}\t {p3quantity.get()}\t {price3}")

            sql = '''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Product-3',p3price.get(),p3quantity.get(),price3))
            connectObj.commit() 

        if p4quantity.get()!=0:
            price4=p4quantity.get()*p1price.get()
            billarea.insert(END,f"\n{dateE.get()}\tProduct-4 \t{p4price.get()}\t {p4quantity.get()}\t {price4}")

            sql = '''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Product-4',p4price.get(),p4quantity.get(),price4))
            connectObj.commit() 

        Totalprice=IntVar()
        Totalprice=price+price2+price3+price4

        Totalquantity=IntVar()
        Totalquantity=p1quantity.get()+p2quantity.get()+p3quantity.get()+p4quantity.get()
        billarea.insert(END,f"\nTotal \t \t  \t{Totalquantity}\t {Totalprice}")

    def view():
      connectObj = db.connect("shopManagement.db")
      cur = connectObj.cursor()  

      sql = 'Select * from Sellings'
      cur.execute(sql)

      rows=cur.fetchall()
      viewarea.insert(END,f"Date\t Product\t  Price of 1\t  Quantity\t  Price\n")
    
    
      for i in rows:
        allrows=""
        for j in i:
            allrows+=str(j)+'\t'
        allrows+='\n'
        viewarea.insert(END,allrows)

    dateL=Label(root,text="Date",bg="DodgerBlue2",width=12,font=('arial',15,'bold'))
    dateL.grid(row=0,column=0,padx=7,pady=7)

    dateE=DateEntry(root,width=12,font=('arial',15,'bold'))
    dateE.grid(row=0,column=1,padx=7,pady=7)

    l=Label(root, text="Product",font=('arial',15,'bold'),bg="DodgerBlue2",width=12)
    l.grid(row=1,column=0,padx=7,pady=7)

    l=Label(root, text="Price",font=('arial',15,'bold'),bg="DodgerBlue2",width=12)
    l.grid(row=1,column=1,padx=7,pady=7)

    l=Label(root, text="Quantity",font=('arial',15,'bold'),bg="DodgerBlue2",width=12)
    l.grid(row=1,column=2,padx=7,pady=7)

#----product 1----------------------------------------------------
    p1name=StringVar()
    p1name.set('Product1')

    p1price=IntVar()
    p1price.set(100)

    p1quantity=IntVar()
    p1quantity.set(0)

    l=Label(root, text=p1name.get(),font=('arial',15,'bold'),width=12)
    l.grid(row=2,column=0,padx=7,pady=7)

    l=Label(root, text=p1price.get(),font=('arial',15,'bold'),width=12)
    l.grid(row=2,column=1,padx=7,pady=7)
 
    t=Entry(root,textvariable=p1quantity,font=('arial',15,'bold'),width=12)
    t.grid(row=2,column=2,padx=7,pady=7)
 
#----product 2-------------------------------------------------------------
    p2name=StringVar()
    p2name.set('Product2')

    p2price=IntVar()
    p2price.set(200)

    p2quantity=IntVar()
    p2quantity.set(0)

    l=Label(root, text=p2name.get(),font=('arial',15,'bold'),width=12)
    l.grid(row=3,column=0,padx=7,pady=7)

    l=Label(root, text=p2price.get(),font=('arial',15,'bold'),width=12)
    l.grid(row=3,column=1,padx=7,pady=7)

    t=Entry(root,textvariable=p2quantity,font=('arial',15,'bold'),width=12)
    t.grid(row=3,column=2,padx=7,pady=7)

#----product 3----
    p3name=StringVar()
    p3name.set('Product3')

    p3price=IntVar()
    p3price.set(300)

    p3quantity=IntVar()
    p3quantity.set(0)

    l=Label(root, text=p3name.get(),font=('arial',15,'bold'),width=12)
    l.grid(row=4,column=0,padx=7,pady=7)

    l=Label(root, text=p3price.get(),font=('arial',15,'bold'),width=12)
    l.grid(row=4,column=1,padx=7,pady=7)

    t=Entry(root,textvariable=p3quantity,font=('arial',15,'bold'),width=12)
    t.grid(row=4,column=2,padx=7,pady=7)

#----product 4----
    p4name=StringVar()
    p4name.set('Product4')

    p4price=IntVar()
    p4price.set(400)

    p4quantity=IntVar()
    p4quantity.set(0)

    l=Label(root, text=p4name.get(),font=('arial',15,'bold'),width=12)
    l.grid(row=5,column=0,padx=7,pady=7)

    l=Label(root, text=p4price.get(),font=('arial',15,'bold'),width=12)
    l.grid(row=5,column=1,padx=7,pady=7)

    t=Entry(root,textvariable=p4quantity,font=('arial',15,'bold'),width=12)
    t.grid(row=5,column=2,padx=7,pady=7)

#------------------------bill-------------------------
    billarea=Text(root)

    submitbtn=Button(root,command=GenerateBill,text="Bill",
    font=('arial',15,'bold'),bg="DodgerBlue2",width=20 )

    submitbtn.grid(row=6,column=0,padx=7,pady=7)

    viewbtn=Button(root,command=view,text="View All Sellings",
    font=('arial',15,'bold'),bg="DodgerBlue2",width=20 )

    viewbtn.grid(row=6,column=2,padx=7,pady=7)

    billarea.grid(row=9,column=0)
    viewarea=Text(root)
    viewarea.grid(row=9,column=2)
#----------------------------------------------tab2 ----------------------------------
    def connection2():
      connectObj2 = db.connect("shopManagement.db")
      cur = connectObj2.cursor()
      sql = '''
    create table if not exists stocks (
        date string,
        product string,
        price number,
        quantity number
        )
    '''
      cur.execute(sql)
      connectObj2.commit()   

    connection2() 

    def addStock():
      global dateE2,qty,name,price

      connectObj = db.connect("shopManagement.db")
      cur = connectObj.cursor()  
      sql = '''
            INSERT INTO stocks VALUES 
            (?, ?, ?, ?)
            '''
      cur.execute(sql,(dateE2.get(),name.get(),price.get(),qty.get()))
      connectObj.commit() 

    def viewStock():
      connectObj = db.connect("shopManagement.db")
      cur = connectObj.cursor()  

      sql = 'Select * from stocks'
      cur.execute(sql)

      rows=cur.fetchall()
      viewarea2.insert(END,f"Date \tProduct\t  Price\t  Quantity\t \n")
    
      for i in rows:
        allrows=""
        for j in i:
            allrows+=str(j)+'\t'
        allrows+='\n'
        viewarea2.insert(END,allrows)

    dateL=Label(root2,text="Date",bg="DodgerBlue2",width=12,font=('arial',15,'bold'))
    dateL.grid(row=0,column=0,padx=7,pady=7)

    dateE2=DateEntry(root2,width=12,font=('arial',15,'bold'))
    dateE2.grid(row=0,column=1,padx=7,pady=7)

    l=Label(root2, text="Product",font=('arial',15,'bold'),bg="DodgerBlue2",width=12)
    l.grid(row=1,column=0,padx=7,pady=7)

    l=Label(root2, text="Price",font=('arial',15,'bold'),bg="DodgerBlue2",width=12)
    l.grid(row=2,column=0,padx=7,pady=7)

    l=Label(root2, text="Quantity",font=('arial',15,'bold'),bg="DodgerBlue2",width=12)
    l.grid(row=3,column=0,padx=7,pady=7)

    name=StringVar()
    price=IntVar()
    qty=IntVar()

    Name=Entry(root2,textvariable=name,font=('arial',15,'bold'),width=12)
    Name.grid(row=1,column=1,padx=7,pady=7)

    Price=Entry(root2,textvariable=price,font=('arial',15,'bold'),width=12)
    Price.grid(row=2,column=1,padx=7,pady=7)

    Qty=Entry(root2,textvariable=qty,font=('arial',15,'bold'),width=12)
    Qty.grid(row=3,column=1,padx=7,pady=7)

    addbtn=Button(root2,command=addStock,text="Add",
    font=('arial',15,'bold'),bg="DodgerBlue2",width=20)

    addbtn.grid(row=4,column=1,padx=7,pady=7)

    viewarea2=Text(root2)
    viewarea2.grid(row=5,column=0,columnspan=2)

    viewbtn2=Button(root2,command=viewStock,text="View Stock",
    font=('arial',15,'bold'),bg="DodgerBlue2",width=20 )

    viewbtn2.grid(row=4,column=0,padx=7,pady=7)



    mainloop()

    

main_account_screen()


