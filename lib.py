#library management system
import mysql.connector
import datetime
con=mysql.connector.connect(user='root',host='localhost', password='HARpreet@kamboj0534')
mycursor=con.cursor()
mycursor.execute("use db3")
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Library Management System")
root.geometry("1050x600")
img=Image.open("library.png")
bck_end=ImageTk.PhotoImage(img)
lbl=Label(root,image=bck_end)
lbl.place(x=0,y=0)
def fxn1():
    t1.delete(1.0,END)
    mycursor.execute("select * from books")
    rows= mycursor.fetchall()
    for row in rows: 
        book_id,name,author,copies = row
        t1.insert(END,f'ID: {book_id} | Title: {name} | Author: {author}\n')
        
def fxn2():
    window2=Toplevel(root)
    window2.title('Issue a Book')
    window2.geometry('700x500')
    window2.resizable(0,0)
    def fxn21():
        a=int(e21.get())
        b=int(e22.get())
        c=datetime.datetime.now()
        a1=[a]
        copies="select copies from books where bookid = %s"
        mycursor.execute(copies,a1)
        d=mycursor.fetchall()
        for item in d:
            for i in item:
                totalcopies=i
        if totalcopies>0:
            comm21="insert into books_issued(studentid,bookid,issuedate) values(%s,%s,%s)"
            issued_data=(b,a,c)
            mycursor.execute(comm21,issued_data)
            update="update books set copies=copies-1 where bookid = %s"
            mycursor.execute(update,a1)
            con.commit()
            t21.insert(INSERT,"Book is issued")
        else:
            t21.insert(INSERT,"Book is currently unavailable")
    l21=Label(window2,text="Enter a book id",bg='black',fg='yellow',font=('italic',15,'bold'),width=20)
    l21.grid(column=0,row=0)
    e21=Entry(window2,width=20,font=('italic',15))
    e21.grid(row=0,column=1)
    l22=Label(window2,text="Enter a student id",bg='black',fg="yellow",font=('italic',15,'bold'),width=20)
    l22.grid(row=1,column=0)
    e22=Entry(window2,width=20,font=('italic',15))
    e22.grid(row=1,column=1)
    b21=Button(window2,text="ISSUE",fg='white',bg='black',font=('italic',15,'bold'),width=10,command=fxn21)
    b21.grid(row=0,column=2)
    t21=Text(window2,width=30,height=30,wrap=WORD)
    t21.grid(row=2,column=1)
def fxn3():
    window3=Toplevel(root)
    window3.title('Add a Book')
    window3.geometry('700x500')
    window3.resizable(0,0)
    def fxn31():
        a=int(e31.get())
        b=e32.get()
        c=e33.get()
        d=int(e34.get())
        comm31="insert into books values(%s,%s,%s,%s)"
        insertdata=(a,b,c,d)
        mycursor.execute(comm31,insertdata)
        con.commit()
        l34.config(text='Inserted successfully!!')
    l31=Label(window3,text='Add Book ID',bg='black',fg='yellow',font=('italic',15,'bold'),width=20)
    l31.grid(row=0,column=0)
    e31=Entry(window3,width=20,font=('italic',15))
    e31.grid(row=0,column=1)
    l32=Label(window3,text='Enter Book name',bg='black',fg='yellow',font=('italic',15,'bold'),width=20)
    l32.grid(row=1,column=0)
    e32=Entry(window3,width=20,font=('italic',15))
    e32.grid(row=1,column=1)
    l33=Label(window3,text='Enter author of book',bg='black',fg='yellow',font=('italic',15,'bold'),width=20)
    l33.grid(row=2,column=0)
    e33=Entry(window3,width=20,font=('italic',15))
    e33.grid(row=2,column=1)
    l34=Label(window3,text='No. of copies available',bg='black',fg='yellow',font=('italic',15,'bold'),width=20)
    l34.grid(row=3,column=0)
    e34=Entry(window3,width=20,font=('italic',15))
    e34.grid(row=3,column=1)
    b31=Button(window3,text='INSERT A BOOK DATA',bg='black',fg='white',font=('italic',15,'bold'),width=20,command=fxn31)
    b31.grid(row=4,column=0)
    l34=Label(window3,fg='black',font=('italic',15,'bold'),width=40)
    l34.grid(row=4,column=1)
def fxn4():
    window2=Toplevel(root)
    window2.title('Return a Book')
    window2.geometry('700x500')
    window2.resizable(0,0)
    def fxn41():
        a=int(e41.get())
        b=int(e42.get())
        c=datetime.datetime.now()
        a1=[a]
        try:
            comm41="update books_issued set returndate =%s where studentid=%s and bookid=%s "
            returndata=(c,b,a)
            mycursor.execute(comm41,returndata)
            updatebook="update books set copies=copies+1 where bookid =%s"
            mycursor.execute(updatebook,a1)
            con.commit()
            l43.config(text="Book is returned")
        except:
            l43.config(text="No issued data of book is present")
    l41=Label(window2,text="Enter a book id",bg='black',fg='yellow',font=('italic',15,'bold'),width=20)
    l41.grid(column=0,row=0)
    e41=Entry(window2,width=20,font=('italic',15))
    e41.grid(row=0,column=1)
    l42=Label(window2,text="Enter a student id",bg='black',fg="yellow",font=('italic',15,'bold'),width=20)
    l42.grid(row=1,column=0)
    e42=Entry(window2,width=20,font=('italic',15))
    e42.grid(row=1,column=1)
    b41=Button(window2,text="RETURN",fg='white',bg='black',font=('italic',15,'bold'),width=10,command=fxn41)
    b41.grid(row=2,column=0)
    l43=Label(window2,fg="black",font=('italic',15,'bold'),width=40)
    l43.grid(row=2,column=1)
def fxn5():
    t1.delete(1.0,END)
    a=int(e1.get())
    a1=[a]
    b="select * from students_details left join books_issued on students_details.studentid = books_issued.studentid where students_details.studentid = %s"
    mycursor.execute(b,a1)
    rows= mycursor.fetchall()
    t1.insert(INSERT,"Students detail:")
    for row in rows: 
        studnetid,name,branch,Class,studentid,book_id,issuedate,returndate = row
        t1.insert(END,f'Student id : {studentid} | Name : {name} | Branch : {branch} | Class : {Class} | Book id: {book_id} | Issue date: {issuedate} | Return date: {returndate}\n')
def fxn6():
    t1.delete(1.0,END)
    a=int(e2.get())
    a1=[a]
    b="select * from books left join books_issued on books.bookid = books_issued.bookid where books.bookid= %s"
    mycursor.execute(b,a1)
    rows= mycursor.fetchall()
    t1.insert(INSERT,"Book details:")
    for row in rows: 
        bookid,title,author,copies,studentid,bookid,issuedate,returndate = row
        t1.insert(END,f'Book id : {bookid} | Title : {title} | Author : {author} | Copies : {copies}|Student id: {studentid} | Issue date: {issuedate} | Return date: {returndate}\n')

l1=Label(root,text="Welcome to College Library!!",bg="black",fg="white",font=("strikeout",30,"underline"),borderwidth=2,relief="solid")
l1.grid(row=0,column=3)
l2=Label(root,text="Enter Student ID",fg="black",bg="lavender",font=("italic",15,"bold"),borderwidth=1,relief="solid", width=15)
l2.grid(row=3,column=2)
e1=Entry(root,font=("italic",15),width=20)
e1.grid(row=3,column=3)
l3=Label(root,text="Enter a Book ID",fg="black",bg="lavender",font=("italic",15,"bold"),borderwidth=1,relief="solid", width=15)
l3.grid(row=5,column=2)
e2=Entry(root,font=("italic",15),width=20)
e2.grid(row=5,column=3)
l4= Label(root,text="OR",fg="black",font=("italic",15))
l4.grid(row=4,column=2)
b1=Button(root,text="List of all Book",fg="white",bg="black",font=("italic",18,"bold"),width=12,command=fxn1)
b1.grid(row=4,column=5)
b2=Button(root,text="Issue a Book",fg="white",bg="black",font=("italic",18,"bold"),width=12,command=fxn2)
b2.grid(row=5,column=5)
b3=Button(root,text="Add a Book",fg="white",bg="black",font=("italic",18,"bold"),width=12,command=fxn3)
b3.grid(row=6,column=5)
b4=Button(root,text="Return a book",fg="white",bg="black",font=("italic",18,"bold"),width=12,command=fxn4)
b4.grid(row=7,column=5)
b5=Button(root,text="Search",fg="yellow",bg="black",font=("italic",15,"bold"),command=fxn5)
b5.grid(row=3,column=4)
b6=Button(root,text="Search",fg="yellow",bg="black",font=("italic",15,"bold"),command=fxn6)
b6.grid(row=5,column=4)
t1=Text(root)
t1.grid(row=8,column=3)

root.mainloop()