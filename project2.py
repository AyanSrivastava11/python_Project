import tkinter as tk
import sqlite3
from datetime import date
from tkinter import messagebox as mb

con=sqlite3.connect('bu1.db')
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS dg (Ref int,To_db varchar(20),From_db varchar(20),JD varchar(20),operator varchar(20),type varchar(20),capacity varchar(20),fare integer)")
con.commit()
cur.execute("create table if not exists dg1 (Refferal int,Name varchar(20),seats int,Gender varchar(20),age int,phone varchar(10),boarding varchar(20),destination varchar(20),oper varchar(20),now varchar(20),then1 varchar(20),price int)")
con.commit()

root=tk.Tk()
root.geometry('1536x838')
root.configure(bg='white smoke')
root.resizable(False,False)
y=tk.IntVar()
frame=tk.Frame(root)

frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=2)
frame.rowconfigure(1,weight=1)

frame2=tk.Frame(root,bg='white smoke')
frame2.columnconfigure(0,weight=1)
frame2.rowconfigure(2,weight=2)
frame2.rowconfigure(3,weight=2)
frame2.rowconfigure(4,weight=2)
frame2.rowconfigure(5,weight=1)
frame2.rowconfigure(6,weight=1)
frame2.rowconfigure(7,weight=2)

Home=tk.PhotoImage(file="home.png")
Dis=tk.PhotoImage(file="dis.png")
photo1=tk.PhotoImage(file='starbus.png')
label0=tk.Label(frame,image=photo1,bg='white')
label0.grid(row=0,column=0,pady=10)
label1=tk.Label(frame,text='Online Bus Booking System',font=('Constantia',30),fg='black',bg='light blue')
label1.grid(row=1,column=0,pady=10)

def tab1():
    def tab2():
        
        frame1=tk.Frame(root,background='white smoke')
        frame1.columnconfigure(0,weight=1)
        frame1.columnconfigure(1,weight=1)
        frame1.columnconfigure(2,weight=1)
        frame1.rowconfigure(2,weight=1)
        frame1.rowconfigure(3,weight=1)
        frame1.rowconfigure(4,weight=1)
        
        label2.destroy()
        label3.destroy()
        label4.destroy()
        label5.destroy()
        label6.destroy()
        button1.destroy()
        frame2.destroy()
        
                
        def tabC3():
            frame1.destroy()
            la1 = tk.Label(root, text='Edit Database', font=(
                'Constantia', 25, 'bold'), bg='black', fg='white')
            la1.pack(pady=15)
            fm1 = tk.Frame(root, background='white smoke')
            fm1.columnconfigure(0, weight=1)
            fm1.columnconfigure(1, weight=1)
            fm1.columnconfigure(2, weight=1)
            fm1.columnconfigure(3, weight=1)

            def delete():
                def bulk():
                    if 'scroll_bar1' in globals() and 'mylist1' in globals():
                        scroll_bar1.destroy()
                        mylist1.destroy()
                        bbb8.destroy()
                    f10.destroy()
                    la2.destroy()
                    buttn6.destroy()
                    buttn8.destroy()
                    but9.destroy()
                    tab2()
                btn6.destroy()
                fm1.destroy()
                la1.destroy()
                la2 = tk.Label(root, text='Enter Bus Details', font=(
                    'Constantia', 25, 'bold'), bg='black', fg='white')
                la2.pack(pady=15)
                f10 = tk.Frame(root, bg='#f05d5d')
                f10.columnconfigure(0, weight=10)
                f10.columnconfigure(1, weight=1)
                f10.columnconfigure(2, weight=1)
                f10.columnconfigure(3, weight=1)
                f10.columnconfigure(4, weight=10)
                lo = tk.Label(f10, text='Enter Ref no.', bg='#f05d5d',
                              fg='black', font=('Arial', 16, 'bold'))
                lo.grid(row=0, column=1)
                e0 = tk.Entry(f10)
                e0.grid(row=0, column=2)
                but9=tk.Button(f10,image=Home,command=bulk) 
                but9.grid(row=0,column=3)
                
                f10.pack(fill='x', pady=20)
                cur.execute("select count(*) from dg")
                cks = cur.fetchone()[0]

                def show3():
                    buttn6['state'] = tk.DISABLED

                    def back4():
                        bbb8.destroy()
                        if 'scroll_bar1' in globals() and 'mylist1' in globals():
                            scroll_bar1.destroy()
                            mylist1.destroy()
                        
                        buttn6['state'] = tk.NORMAL
            
                    global scroll_bar1, mylist1,bbb8
                    bbb8 = tk.Button(root, text='Back', command=back4, font=(
                        'Times_New_Roman', 11, 'bold'), bg='white', activebackground='red')
                    bbb8.pack()
                    scroll_bar1 = tk.Scrollbar(root)
                    scroll_bar1.pack(side='right', fill='y')
                    mylist1 = tk.Listbox(root, yscrollcommand=scroll_bar1.set)
                    cur.execute("select * from dg")
                    for line in range(1, cks+1):
                        mylist1.insert('end', cur.fetchone())
                    mylist1.pack(side='left', fill='both', expand=True)
                    scroll_bar1.config(command=mylist1.yview)
                def fun2():
                    global scroll_bar1
                    cur.execute("delete from dg where Ref = ?",([e0.get()]))
                    con.commit()
                    aaa=tk.messagebox.askquestion("Check", "Are you sure ?")
                    if(aaa=='yes'):
                        if(mb.showinfo('Success','Bus deleted successfully')):
                           f10.destroy()
                           la2.destroy()
                           buttn6.destroy()
                           buttn8.destroy()
                           if 'scroll_bar1' in globals() and 'mylist1' in globals():
                               scroll_bar1.destroy()
                               mylist1.destroy()
                               bbb8.destroy()
                               delete()
                           else:
                               delete()
           
                buttn8 = tk.Button(root, text='Delete', font=('Times_New_Roman', 15, 'bold'), command=fun2,bg='white', activebackground='red')
                buttn8.pack(padx=10)
                buttn6 = tk.Button(root, text='Show Database', command=show3, font=(
                      'Times_New_Roman', 11, 'bold'), bg='white', activebackground='red')
                buttn6.pack(padx=10,pady=7)    

            def add():
                def bulk1():
                    if 'scroll_bar' in globals() and 'mylist' in globals():
                           scroll_bar.destroy()
                           mylist.destroy()
                           buttn7.destroy()
                    f9.destroy()
                    la2.destroy()
                    buttn6.destroy()
                    buttn8.destroy()
                    buttn9.destroy()
                    tab2()
                btn6.destroy()
                fm1.destroy()
                la1.destroy()
                la2 = tk.Label(root, text='Add Bus Details', font=(
                    'Constantia', 25, 'bold'), bg='black', fg='white')
                la2.pack(pady=15)
                f9 = tk.Frame(root, bg='#f05d5d')
                f9.columnconfigure(0, weight=1)
                f9.columnconfigure(1, weight=1)
                f9.columnconfigure(2, weight=1)
                f9.columnconfigure(3, weight=1)
                f9.columnconfigure(4, weight=1)
                f9.columnconfigure(5, weight=1)
                f9.columnconfigure(6, weight=1)
                f9.columnconfigure(7, weight=1)
                f9.columnconfigure(8, weight=1)
                f9.columnconfigure(9, weight=1)
                f9.columnconfigure(10, weight=1)
                f9.columnconfigure(11, weight=1)
                f9.columnconfigure(12, weight=1)
                f9.columnconfigure(13, weight=1)
                f9.columnconfigure(14, weight=1)

                lol8 = tk.Label(f9, text='Operator', bg='#f05d5d',
                                fg='black', font=('Arial', 10, 'bold'))
                lol8.grid(row=0, column=0)
                er3 = tk.Entry(f9)
                er3.grid(row=0, column=1)
                lol9 = tk.Label(f9, text='Type', bg='#f05d5d',
                                fg='black', font=('Arial', 10, 'bold'))
                lol9.grid(row=0, column=2)
                options1 = tk.StringVar()
                options1.set('2x2(Non_AC)')
                op2 = tk.OptionMenu(f9, options1, '2x2(Non_AC)',
                                    '2x2(AC)', '1x1(Non_AC)', '1x1(AC)')
                op2.grid(row=0, column=3)
                lol10 = tk.Label(f9, text='Capacity', bg='#f05d5d',
                                 fg='black', font=('Arial', 10, 'bold'))
                lol10.grid(row=0, column=4)
                er5 = tk.Entry(f9)
                er5.grid(row=0, column=5)
                lol12 = tk.Label(f9, text='Journey Date', bg='#f05d5d',
                                 fg='black', font=('Arial', 10, 'bold'))
                lol12.grid(row=0, column=6)
                er6 = tk.Entry(f9)
                er6.grid(row=0, column=7)
                lol14 = tk.Label(f9, text='Fare', bg='#f05d5d',
                                 fg='black', font=('Arial', 10, 'bold'))
                lol14.grid(row=0, column=8)
                er8 = tk.Entry(f9)
                er8.grid(row=0, column=9)
                lol14 = tk.Label(f9, text='To', bg='#f05d5d',
                                 fg='black', font=('Arial', 10, 'bold'))
                lol14.grid(row=0, column=10)
                er9 = tk.Entry(f9)
                er9.grid(row=0, column=12)
                lol14 = tk.Label(f9, text='From', bg='#f05d5d',
                                 fg='black', font=('Arial', 10, 'bold'))
                lol14.grid(row=0, column=13)
                er10 = tk.Entry(f9)
                er10.grid(row=0, column=14)
                f9.pack(fill='x', pady=20)
                cur.execute("select count(*) from dg")
                cks = cur.fetchone()[0]

                def show2():
                    buttn6['state'] = tk.DISABLED
                    def back3():
                        buttn7.destroy()
                        if 'scroll_bar' in globals() and 'mylist' in globals():
                            scroll_bar.destroy()
                            mylist.destroy()
                        
                        buttn6['state'] = tk.NORMAL
            
                    global scroll_bar, mylist,buttn7
                    buttn7 = tk.Button(root, text='Back', command=back3, font=(
                        'Times_New_Roman', 11, 'bold'), bg='white', activebackground='red')
                    buttn7.pack()
                    scroll_bar = tk.Scrollbar(root)
                    scroll_bar.pack(side='right', fill='y')
                    mylist = tk.Listbox(root, yscrollcommand=scroll_bar.set)
                    cur.execute("select * from dg")
                    for line in range(1, cks+1):
                        mylist.insert('end', cur.fetchone())
                    mylist.pack(side='left', fill='both', expand=True)
                    scroll_bar.config(command=mylist.yview)

                def fun1():
                    global scroll_bar
                    cur.execute("select count(*) from dg")
                    cnt2 = cur.fetchone()[0]
                    print(cnt2)
                    cur.execute("select Ref from dg")
                    ref2 = cur.fetchmany(cnt2)[cnt2-1][0]
                    cur.execute("insert into dg values (?,?,?,?,?,?,?,?)", (ref2+1, er9.get(),
                                er10.get(), er6.get(), er3.get(), options1.get(), er5.get(), er8.get()))
                    con.commit()
                    cur.execute("select * from dg where Ref=?", [ref2+1])
                    print(cur.fetchall())
                    if(tk.messagebox.showinfo("Success", "Bus Added Successfully")):
                        f9.destroy()
                        la2.destroy()
                        buttn6.destroy()
                        buttn8.destroy()
                        buttn9.destroy()
                        if 'scroll_bar' in globals() and 'mylist' in globals():
                            scroll_bar.destroy()
                            mylist.destroy()
                            buttn7.destroy()
                            add()
                        else:
                            add()
                buttn9=tk.Button(root,image=Home,command=bulk1)
                buttn9.place(x=900,y=520)
                buttn8 = tk.Button(root, text='Insert', command=fun1, font=(
                    'Times_New_Roman', 15, 'bold'), bg='white', activebackground='red')
                buttn8.pack(padx=10)
                buttn6 = tk.Button(root, text='Show Database', command=show2, font=(
                    'Times_New_Roman', 11, 'bold'), bg='white', activebackground='red')
                buttn6.pack(padx=10,pady=7)
                    
                    
            buttn3 = tk.Button(fm1, text='Add Bus', font=(
                'Times_New_Roman', 15, 'bold'), bg='white', activebackground='red', command=add)
            buttn3.grid(row=3, column=0)
            buttn4 = tk.Button(fm1, text='Delete Bus', font=(
                'Times_New_Roman', 15, 'bold'), bg='white', activebackground='red', command=delete)
            buttn4.grid(row=3, column=1)
            buttn5 = tk.Button(fm1, text='Edit Route', font=(
                'Times_New_Roman', 15, 'bold'), bg='white', activebackground='red')
            buttn5.grid(row=3, column=2)
            buttn5 = tk.Button(fm1, text='Edit Journey Date', font=(
                'Times_New_Roman', 15, 'bold'), bg='white', activebackground='red')
            buttn5.grid(row=3, column=3)
            def tkHome():
                fm1.destroy()
                la1.destroy()
                btn6.destroy()
                tab2()
            btn6=tk.Button(root,image=Home,command=tkHome)
            btn6.place(x=750,y=650)
            fm1.pack(fill='both', expand=True, pady=40)
        def tabB3():
            la1=tk.Label(root,text='Check Your Booking',font=('Constantia',20,'bold'),bg='light blue',fg='red')
            la1.pack(pady=30)
            frame1.destroy()
            frame8=tk.Frame(root,bg='white smoke',pady=20)
            frame8.columnconfigure(0,weight=8)
            frame8.columnconfigure(1,weight=1)
            frame8.columnconfigure(2,weight=1)
            frame8.columnconfigure(3,weight=1)
            frame8.columnconfigure(4,weight=8)
            l2=tk.Label(frame8,text='Enter Your Mobile No.',bg='white smoke',fg='Black',font=('Arial',14,'bold'))
            l2.grid(row=0,column=1)
            e0=tk.Entry(frame8)
            e0.grid(row=0,column=2)
            def hore():
                frame8.destroy()
                la1.destroy()
                yyy.destroy()
                tab2()
            yyy=tk.Button(frame8,image=Home,command=hore)
            yyy.grid(row=0,column=4)
            
            def book():
                cur.execute("select count(*) from dg1 where phone=?",([e0.get()]))
                if(cur.fetchmany(1)[0][0]==0):
                    if(tk.messagebox.showerror("Invalid","No such Entry found")):
                        res1=tk.messagebox.askquestion("Add","Do you want to book now?")
                        if(res1=='yes'):
                            la1.destroy()
                            frame8.destroy()
                            tab3()
               
                else:
                    va1=str(e0.get())
                    print(va1)
                    la1.destroy()
                    frame8.destroy()
                    lb=tk.Label(root,text='Bus Ticket',font=('Constantia',20,'bold'),bg='light blue',fg='red')
                    lb.pack(pady=25)
                    frame9=tk.Frame(root,bg='white',bd=5,relief=tk.SUNKEN)
                    frame9.columnconfigure(0,weight=1)
                    frame9.columnconfigure(1,weight=1)
                    
                    
                    cur.execute("select Refferal from dg1 where phone=?",[va1])
                    Nam0=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select Name from dg1 where phone=?",[va1])
                    Nam2=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select seats from dg1 where phone=?",[va1])
                    Nam3=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select Gender from dg1 where phone=?",[va1])
                    Nam4=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select age from dg1 where phone=?",[va1])
                    Nam5=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select phone from dg1 where phone=?",[va1])
                    Nam6=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select boarding from dg1 where phone=?",[va1])
                    Nam7=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select oper from dg1 where phone=?",[va1])
                    Nam8=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select now from dg1 where phone=?",[va1])
                    Nam9=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select then1 from dg1 where phone=?",[va1])
                    Nam10=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select price from dg1 where phone=?",[va1])
                    Nam11=cur.fetchmany(1)[0][0]
                    
                    cur.execute("select destination from dg1 where phone=?",[va1])
                    Nam12=cur.fetchmany(1)[0][0]
                    
                    lb=tk.Label(frame9,text='Passenger: '+Nam2.capitalize(),font=('Times',15,'bold'),bg='white')
                    lb.grid(column=0,row=0)
                    lb1=tk.Label(frame9,text='No. of Seats: '+str(Nam3),font=('Times',15,'bold'),bg='white')
                    lb1.grid(column=0,row=1)
                    lb2=tk.Label(frame9,text='Age: '+str(Nam5),font=('Times',15,'bold'),bg='white')
                    lb2.grid(column=0,row=2)
                    lb3=tk.Label(frame9,text='Travel On: '+Nam10,font=('Times',15,'bold'),bg='white')
                    lb3.grid(column=0,row=3)
                    lb4=tk.Label(frame9,text='Refferal.: '+str(Nam0),font=('Times',15,'bold'),bg='white')
                    lb4.grid(column=0,row=4)
                    lb5=tk.Label(frame9,text='Destination: '+Nam12.capitalize(),font=('Times',15,'bold'),bg='white')
                    lb5.grid(column=0,row=5)
                    lb6=tk.Label(frame9,text='Gender: '+Nam4.capitalize(),font=('Times',15,'bold'),bg='white')
                    lb6.grid(column=1,row=0)
                    lb7=tk.Label(frame9,text='Phone: '+Nam6,font=('Times',15,'bold'),bg='white')
                    lb7.grid(column=1,row=1)
                    lb8=tk.Label(frame9,text='*Fare: '+str(Nam11)+'(each)',font=('Times',15,'bold'),bg='white')
                    lb8.grid(column=1,row=2)
                    lb9=tk.Label(frame9,text='Bus Detail: '+Nam8.capitalize(),font=('Times',15,'bold'),bg='white')
                    lb9.grid(column=1,row=3)
                    lb10=tk.Label(frame9,text='Booked On: '+Nam9,font=('Times',15,'bold'),bg='white')
                    lb10.grid(column=1,row=4)
                    lb11=tk.Label(frame9,text='Boarding Point: '+Nam7.capitalize(),font=('Times',15,'bold'),bg='white')
                    lb11.grid(column=1,row=5)
                    frame10=tk.Frame(frame9,bg='red')
                    frame10.columnconfigure(0,weight=1)
                    l1=tk.Label(frame10,text='*Total amount of '+str(Nam11*Nam3)+' is to be paid at the time of boarding',font=('Arial',15),fg='red')
                    l1.grid(row=0,column=0)
                    frame10.grid(row=6,column=0,columnspan=2)
                    frame9.pack()
               
            butn1=tk.Button(frame8,text='Check Booking',font=('Arial',14,'bold'),activebackground='#0404ba',command=book)
            butn1.grid(row=0,column=3)
            frame8.pack(fill='both',expand=True) 
            
        def tab3():    
            
            button4.destroy()
            button3.destroy()
            button5.destroy()
            lab=tk.Label(root,text='Enter Journey Details',font=('Constantia',20,'bold'),bg='light blue',fg='red')
            lab.pack(pady=10)
           
            frame1.destroy()
            
            frame3=tk.Frame(root,bg='white smoke')
            frame3.columnconfigure(0,weight=1)
            frame3.columnconfigure(1,weight=1)
            frame3.columnconfigure(2,weight=1)
            frame3.columnconfigure(3,weight=1)
            frame3.columnconfigure(4,weight=1)
            frame3.columnconfigure(5,weight=1)
            frame3.columnconfigure(6,weight=2)
            frame3.columnconfigure(7,weight=3)
            
            
            lab1=tk.Label(frame3,text='To',bg='white smoke',fg='Black',font=('Arial',10,'bold'))
            lab1.grid(row=0,column=0)
            entry=tk.Entry(frame3)
            entry.grid(row=0,column=1)
            lab2=tk.Label(frame3,text='From',bg='white smoke',fg='Black',font=('Arial',10,'bold'))
            lab2.grid(row=0,column=2)
            entry1=tk.Entry(frame3)
            entry1.grid(row=0,column=3)
            lab3=tk.Label(frame3,text='Journey Date',bg='white smoke',fg='Black',font=('Arial',10,'bold'))
            lab3.grid(row=0,column=4)
            entry2=tk.Entry(frame3)
            entry2.grid(row=0,column=5)
            def del1():
                lab.destroy()
                frame3.destroy()
                tab2()
            def show():
                cur.execute("select count(*) from dg where To_db=? and From_db=? and JD=?",(entry.get(),entry1.get(),entry2.get()))
                count3=(cur.fetchone()[0])
                print(count3)
                if(count3==0):
                    tk.messagebox.showerror("Error","No Such Bus Found")
                if(count3)!=0:
                    but1['state']=tk.DISABLED
                    but1['image']=Dis
                frame4=tk.Frame(root,bg='white smoke')
                frame4.columnconfigure(0,weight=1)
                frame4.columnconfigure(1,weight=1)
                frame4.columnconfigure(2,weight=1)
                frame4.columnconfigure(3,weight=1)
                frame4.columnconfigure(4,weight=1)
                frame4.columnconfigure(5,weight=1)
                lab4=tk.Label(frame4,text='Select Bus',font=('Rosewood_Std_Fill',8,'bold'),bg='white smoke')
                lab4.grid(row=0,column=0)
                lab4=tk.Label(frame4,text='Operator',font=('Rosewood_Std_Fill',8,'bold'),bg='white smoke')
                lab4.grid(row=0,column=1)
                lab4=tk.Label(frame4,text='Bus Type',font=('Rosewood_Std_Fill',8,'bold'),bg='white smoke')
                lab4.grid(row=0,column=2)
                lab4=tk.Label(frame4,text='Available Capacity',font=('Rosewood_Std_Fill',8,'bold'),bg='white smoke')
                lab4.grid(row=0,column=3)
                lab4=tk.Label(frame4,text='Fair',font=('Rosewood_Std_Fill',8,'bold'),bg='white smoke')
                lab4.grid(row=0,column=4)
                
                def back():
                    but1['state']=tk.NORMAL
                    but1['image']=Home
                    frame4.destroy()
                
               
                ent1=entry.get()
                ent2=entry1.get()
                ent3=entry2.get()
                cur.execute("select count(*) from dg where To_db=? and From_db=? and JD=?",(ent1,ent2,ent3))
                count=(cur.fetchone()[0])
                x=tk.IntVar()
                
                def pass1():
                    bt1['state']=tk.DISABLED
                    lab11=tk.Label(root,text='Fill Passenger Details to book the bus ticket',font=('Constantia',20,'bold'),bg='light blue',fg='red')
                    lab11.pack(pady=30)
                    frame5=tk.Frame(root,bg='white smoke')
                    frame5.columnconfigure(0,weight=1)
                    frame5.columnconfigure(1,weight=1)
                    frame5.columnconfigure(2,weight=1)
                    frame5.columnconfigure(3,weight=1)
                    frame5.columnconfigure(4,weight=1)
                    frame5.columnconfigure(5,weight=1)
                    frame5.columnconfigure(6,weight=1)
                    frame5.columnconfigure(7,weight=1)
                    frame5.columnconfigure(8,weight=1)
                    frame5.columnconfigure(9,weight=1)
                    frame5.columnconfigure(10,weight=1)
                    frame5.columnconfigure(11,weight=1)
                    
                   
                    
                    lab8=tk.Label(frame5,text='Name',bg='white smoke',fg='Black',font=('Arial',10,'bold'))
                    lab8.grid(row=0,column=0)
                    entry3=tk.Entry(frame5)
                    entry3.grid(row=0,column=1)
                    lab9=tk.Label(frame5,text='Gender',bg='white smoke',fg='Black',font=('Arial',10,'bold'))
                    lab9.grid(row=0,column=2)
                    options=tk.StringVar()
                    options.set('Male')
                    op1=tk.OptionMenu(frame5,options,'Male','Female','Other')
                    op1.grid(row=0,column=3)
                    lab10=tk.Label(frame5,text='No. of Seats',bg='white smoke',fg='Black',font=('Arial',10,'bold'))
                    lab10.grid(row=0,column=4)
                    entry5=tk.Entry(frame5)
                    entry5.grid(row=0,column=5)
                    lab12=tk.Label(frame5,text='Mobile No.',bg='white smoke',fg='Black',font=('Arial',10,'bold'))
                    lab12.grid(row=0,column=6)
                    entry6=tk.Entry(frame5)
                    entry6.grid(row=0,column=7)
                    lab14=tk.Label(frame5,text='Age',bg='white smoke',fg='Black',font=('Arial',10,'bold'))
                    lab14.grid(row=0,column=8)
                    entry8=tk.Entry(frame5) 
                    entry8.grid(row=0,column=9)
                    def back1():
                        bt1['state']=tk.NORMAL
                        frame5.destroy()
                        lab11.destroy()
                    def tab4():
                        Namee3=entry5.get()
                        cur.execute("select fare from dg where To_db=? and From_db=? and JD=?",(ent1,ent2,ent3))
                        Namee11=cur.fetchmany(count3)[x.get()][0]
                        res = mb.askquestion('Fare Confirm',  
                         'Total amount to be paid Rs '+str(int(Namee11)*int(Namee3)) )
                        if res == 'yes' : 
                            tk.messagebox.showinfo("Success", "Seat Booked") 
                            et=entry3.get()
                            et1=entry5.get()
                            et2=options.get()
                            et3=entry8.get()
                            et4=entry6.get() 
                            cur.execute("select operator from dg where To_db=? and From_db=? and JD=?",(ent1,ent2,ent3))
                            operator1=cur.fetchmany(count)[x.get()][0]
                            print(operator1)
                            now1=date.today()
                            now1=now1.strftime("%d/%m/%Y")
                            print(now1)
                            cur.execute("select fare from dg where To_db=? and From_db=? and JD=?",(ent1,ent2,ent3))
                            price1=cur.fetchmany(count)[x.get()][0]
                            cur.execute("select Ref from dg where To_db=? and From_db=? and JD=?",(ent1,ent2,ent3))
                            type1=cur.fetchmany(count)[x.get()][0]
                            cur.execute("insert into dg1 values(?,?,?,?,?,?,?,?,?,?,?,?)",(int(type1),et,int(et1),et2,int(et3),et4,entry1.get(),entry.get(),operator1,now1,entry2.get(),int(price1)))
                            con.commit()
                            cur.execute("select * from dg1")
                            print(cur.fetchall())
                            frame4.destroy()
                            frame5.destroy()
                            frame3.destroy()
                            lab.destroy()
                            lab11.destroy()
                            lb=tk.Label(root,text='Bus Ticket',font=('Constantia',20,'bold'),bg='light blue',fg='red')
                            lb.pack(pady=25)
                            frame6=tk.Frame(root,bg='white',bd=5,relief=tk.SUNKEN)
                            frame6.columnconfigure(0,weight=1)
                            frame6.columnconfigure(1,weight=1)
                            
                            cur.execute("select count(*) from dg1")
                            count1=cur.fetchmany(1)[0][0]
                            
                            cur.execute("select Refferal from dg1")
                            Name0=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select Name from dg1")
                            Name2=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select seats from dg1")
                            Name3=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select Gender from dg1")
                            Name4=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select age from dg1")
                            Name5=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select phone from dg1")
                            Name6=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select boarding from dg1")
                            Name7=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select oper from dg1")
                            Name8=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select now from dg1")
                            Name9=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select then1 from dg1")
                            Name10=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select price from dg1")
                            Name11=cur.fetchmany(count1)[count1-1][0]
                            
                            cur.execute("select destination from dg1")
                            Name12=cur.fetchmany(count1)[count1-1][0]
                            
                            lb=tk.Label(frame6,text='Passenger: '+Name2.capitalize(),font=('Times',15,'bold'),bg='white')
                            lb.grid(column=0,row=0)
                            lb1=tk.Label(frame6,text='No. of Seats: '+str(Name3),font=('Times',15,'bold'),bg='white')
                            lb1.grid(column=0,row=1)
                            lb2=tk.Label(frame6,text='Age: '+str(Name5),font=('Times',15,'bold'),bg='white')
                            lb2.grid(column=0,row=2)
                            lb3=tk.Label(frame6,text='Travel On: '+Name10,font=('Times',15,'bold'),bg='white')
                            lb3.grid(column=0,row=3)
                            lb4=tk.Label(frame6,text='Ref_No.: '+str(Name0),font=('Times',15,'bold'),bg='white')
                            lb4.grid(column=0,row=4)
                            lb5=tk.Label(frame6,text='Destination: '+Name12.capitalize(),font=('Times',15,'bold'),bg='white')
                            lb5.grid(column=0,row=5)
                            lb6=tk.Label(frame6,text='Gender: '+Name4.capitalize(),font=('Times',15,'bold'),bg='white')
                            lb6.grid(column=1,row=0)
                            lb7=tk.Label(frame6,text='Phone: '+Name6,font=('Times',15,'bold'),bg='white')
                            lb7.grid(column=1,row=1)
                            lb8=tk.Label(frame6,text='*Fare: '+str(Name11)+'(each)',font=('Times',15,'bold'),bg='white')
                            lb8.grid(column=1,row=2)
                            lb9=tk.Label(frame6,text='Bus Detail: '+Name8.capitalize(),font=('Times',15,'bold'),bg='white')
                            lb9.grid(column=1,row=3)
                            lb10=tk.Label(frame6,text='Booked On: '+Name9,font=('Times',15,'bold'),bg='white')
                            lb10.grid(column=1,row=4)
                            lb11=tk.Label(frame6,text='Boarding Point: '+Name7.capitalize(),font=('Times',15,'bold'),bg='white')
                            lb11.grid(column=1,row=5)
                            frame7=tk.Frame(frame6,bg='red')
                            frame7.columnconfigure(0,weight=1)
                            l1=tk.Label(frame7,text='*Total amount of '+str(Name11*Name3)+' is to be paid at the time of boarding',font=('Arial',10),bg='red',fg='#0404ba')
                            l1.grid(row=0,column=0)
                            frame7.grid(row=6,column=0,columnspan=2)
                            def ho():
                                lb.destroy()
                                bk.destroy()
                                frame6.destroy()
                                frame7.destroy()
                                tab2()
                                
                            bk=tk.Button(root,font=('Arial',10,'bold'),activebackground='#0404ba',command=ho,image=Home)
                            bk.place(x=980,y=550)
                            frame6.pack()
                        
                            
                              
                        else : 
                            mb.showinfo('Return', 'Returning to main application') 
      

                      
                    button7=tk.Button(frame5,text='Book Seat',font=('Arial',10,'bold'),activebackground='#0404ba',command=tab4)
                    button7.grid(row=0,column=10)
                    
                    button7=tk.Button(frame5,text='Back',font=('Arial',10,'bold'),activebackground='#0404ba',command=back1)
                    button7.grid(row=1,column=10)
                    
                    frame5.pack(fill='both',expand=True)
                    
                for index in range(count):
                    color1='#0404ba'
                    radbtn=tk.Radiobutton(frame4,text='Bus '+str(index+1),variable=x,value=index,bg=color1,indicatoron=0)
                    radbtn.grid(row=index+1,column=0,pady=5)
                for i in range(count):
                    cur.execute("select operator from dg where To_db=? and From_db=? and JD=?",(ent1,ent2,ent3))
                    Lab5=tk.Label(frame4,text=cur.fetchmany(2)[i][0],font=('Courier',10,'bold'),bg='light blue',fg='red')
                    Lab5.grid(row=i+1,column=1)
                for i in range(count):
                    cur.execute("select type from dg where To_db=? and From_db=? and JD=?",(ent1,ent2,ent3))
                    Lab6=tk.Label(frame4,text=cur.fetchmany(2)[i][0],font=('Courier',10,'bold'),bg='light blue',fg='red')
                    Lab6.grid(row=i+1,column=2)
                for i in range(count):
                    cur.execute("select capacity from dg where To_db=? and From_db=? and JD=?",(ent1,ent2,ent3))
                    Lab7=tk.Label(frame4,text=cur.fetchmany(2)[i][0],font=('Courier',10,'bold'),bg='light blue',fg='red')
                    Lab7.grid(row=i+1,column=3)
                for i in range(count):
                    cur.execute("select fare from dg where To_db=? and From_db=? and JD=?",(ent1,ent2,ent3))
                    Lab7=tk.Label(frame4,text=cur.fetchmany(2)[i][0],font=('Courier',10,'bold'),bg='light blue',fg='red')
                    Lab7.grid(row=i+1,column=4)
                if(count!=0):  
                    
                    button8=tk.Button(frame4,text='Proceed to book',font=('Arial',10,'bold'),activebackground='#0404ba',command=pass1)
                    button8.grid(row=1,column=5)
                    bt1=tk.Button(frame4,text='Back',font=('Arial',10,'bold'),activebackground='#0404ba',command=back)
                    bt1.grid(row=2,column=5)
                    frame4.pack(fill='x')
                
                
            but1=tk.Button(frame3,font=('Arial',10,'bold'),activebackground='#0404ba',command=del1,image=Home)
            but1.grid(row=0,column=7)
            button6=tk.Button(frame3,text='Show Bus',font=('Arial',10,'bold'),activebackground='#0404ba',command=show)
            button6.grid(row=0,column=6)
            
          
            
            frame3.pack(fill='x',pady=10)
            
        button3=tk.Button(frame1,text='Seat Booking',font=('Arial',15,'bold'),command=tab3,bg='red',activebackground='#0404ba')
        button3.grid(row=3,column=0)
        button4=tk.Button(frame1,text='Check Booked Seat',font=('Arial',15,'bold'),command=tabB3,bg='red',activebackground='#0404ba')
        button4.grid(row=3,column=1)
        button5=tk.Button(frame1,text='Add Bus Details',font=('Arial',15,'bold'),bg='red',activebackground='#0404ba',command=tabC3)
        button5.grid(row=3,column=2)
        
        frame1.pack(fill='both',expand=True)
    
    label2=tk.Label(frame2,text='Name: Ayan Srivastava',font=('Arial',15,'bold'),fg='red')
    label2.grid(row=2,column=0,pady=20)
    label3=tk.Label(frame2,text='Er: 221B112',font=('Arial',15,'bold'),fg='red')
    label3.grid(row=3,column=0,pady=20)
    label4=tk.Label(frame2,text='Mobile: 9555305630',font=('Arial',15,'bold'),fg='red')
    label4.grid(row=4,column=0,pady=20)
    label5=tk.Label(frame2,text='Submitted  to: Mahesh Kumar Sir',font=('Constantia',30),fg='black',bg='light blue')
    label5.grid(row=5,column=0,pady=(0,15))
    label6=tk.Label(frame2,text='Project Based Learning',font=('Constantia',15,'bold'),fg='black',bg='light blue')
    label6.grid(row=6,column=0)
    button1=tk.Button(frame2,text='Next',font=('Arial',14,'bold'),activebackground='#0404ba',command=tab2)
    button1.grid(row=7,column=0,pady=20)
frame.pack(fill='both')
frame2.pack(fill='both',expand=True)  

    

tab1()
root.mainloop()
        