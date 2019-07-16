from tkinter import *
import random
import datetime
import time
from tkinter import messagebox
import pymysql
import smtplib
import socket
import sys



def hii ():
        top=Toplevel()
        top.geometry("1350x750")
        top.title("Canteen Management")
        top.configure(background="#000011")

        #======================================history========================================================================
        def client():

                s=socket.socket()
                host="Sparsh"
                port=8080
                s.connect((host,port))
                print("Connected to chat server")
                while 1:
                     incoming_message=s.recv(1024)
                     incoming_message=incoming_message.decode()
                     print(END,"server:%s\n"%incoming_message)
                     print(END,message=input(str(">>")))
                     message=message.encode()
                     s.send(message)
                     print(END,"message has been sent")
                     print("")

        def mail():
                try:
                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login('jecrccanteen@gmail.com','canteenjecrc10')
                    s=""
                    
                    
                    if x1==1:
                        s+='TEA='+txt0.get()+','
                    if x2==1:
                        s+='Black Tea='+txt1.get()+','
                    if x3==1:
                        s+='Green Tea='+txt2.get()+','
                    if x4==1:
                        s+='coffee='+txt3.get()+','
                    if x5==1:
                        s+='Mountain Dew='+txt4.get()+','
                    if x6==1:
                        s+='Sprite='+txt5.get()+','
                    if x7==1:
                        s+='Mirinda='+txt6.get()+','
                    if x8==1:
                        s+='Pepsi='+txt7.get()+','
                    if x9==1:
                        s+='Noodles='+txt8.get()+','
                    if x10==1:
                        s+='Pasta='+txt9.get()+','
                    if x11==1:
                        s+='Pizza='+txt10.get()+','
                    if x12==1:
                        s+='Sandwich='+txt11.get()+','
                    if x13==1:
                        s+='Patties='+txt12.get()+','
                    if x14==1:
                        s+='Burger='+txt13.get()+','
                    
                    if x15==1:
                        s+='samosa='+txt14.get()+','
                    if x16==1:
                        s+='kachori='+txt15.get()+','
                    s+='\n'+'Amount\t\t\t'+Amount.get()+'\n'+'Service Tax(5%)\t\t\t'+Service_Tax.get()+"\n"+'GST(12%)\t\t\t'+GST.get()+"\n"+'Total\t\t\t'+Total.get()
                   
                    s+='\nDATE:'+DateofOrder.get()+'\n'+'RECEIPT_NO.:'+Receipt_Ref.get()+'\n'
                    server.sendmail('jecrccanteen@gmail.com',tv2.get(),s)
                    print("mail sent")
                except Exception as e:
                    print(e)
                s=''
                #=============================================================history============================================================
        def history():
                hist=Toplevel()
                hist.geometry("1350x750")
                hist.title("HISTORY")
                scroll=Scrollbar(hist)
                scroll.pack(side=RIGHT,fill=Y)
                
                text=Text(hist,width=170,height=700,yscrollcommand=scroll.set,fg="white",bg="#000033",cursor="circle")
                text.pack(side=LEFT,fill=BOTH)#  ..................................................
                text.insert(END,"   Receipt_ID\t\t    Date\t\t       Customer Name\t\t\t    Mail_ID\t\t\t      Phone NO.\t\t         Entry\t\t\t\t\t   Amount\n\n\n")
                db=pymysql.connect(user="root",password="Sparshj18@",host="localhost",port=3306,database="canteen")
                mycursor=db.cursor()

                sql="SELECT * FROM receipt"
                try:
                    mycursor.execute(sql)
                   
                    result=mycursor.fetchall()
                    for row in result:
                        freceipt=row[0]
                        fdate=row[1]
                        fname=row[2]
                        fmail=row[3]
                        fphone=row[4]
                        fentry=row[5]
                        famount=row[6]
                    
                    
                        
                        text.insert(END,"-> "+"{0:<19}".format(freceipt)+"{0:<19}".format(fdate)+"{0:<20}".format(fname)+"{0:<27}".format(fmail)\
                                    +"{0:<19}".format(str(int(fphone)))+"{0:<35}".format(fentry)+"{0:<19}".format(str(famount))+"\n")
                                   
                        
                except Exception as e:
                    print(e)
                db.close()
                scroll.config( command=text)
                #===================================================================================================================
        menu = Menu(top)
        top.config(menu=menu)
        submenu1=Menu(menu)
        submenu2=Menu(menu)
        submenu3=Menu(menu)
        menu.add_cascade(label="File",menu=submenu1)
        menu.add_separator()
        submenu1.add_command(label="History",command=history)
        menu.add_cascade(label="Edit",menu=submenu2)
        menu.add_separator()
        menu.add_cascade(label="Format",menu=submenu3)


            # =============================================================arrangement of frames==================================================





        f2=Frame(top,height=70,width=1350,bd=1,relief="raise")
        f2.pack(side="top")
        f2.configure(background="#000033")

        f3=Frame(top,height=650,width=700,bd=1,relief="raise")
        f3.pack(side="left")
        f3.configure(background="#000033")

        f4=Frame(top,height=650,width=650,bd=1,relief="raise")
        f4.pack(side="right")
        f4.configure(background="#000033")

        f3a=Frame(f3,height=100,width=700,bd=1,relief="raise")
        f3a.pack(side="top")
        f3a.configure(background="#000033")

        f3b=Frame(f3,height=550,width=700,bd=1,relief="raise")
        f3b.pack(side="bottom")
        f3b.configure(background="#000033")

        f3ba=Frame(f3b,height=550,width=200,bd=1,relief="raise")
        f3ba.pack(side="left")
        f3ba.configure(background="#000033")


        f3bb=Frame(f3b,height=550,width=500,bd=1,relief="raise")
        f3bb.pack(side="right")
        f3bb.configure(background="#000033")

        f3bba=Frame(f3bb,height=550,width=500,bd=1,relief="raise")
        f3bba.pack(side="right")
        f3bba.configure(background="#000033")

        f4a=Frame(f4,height=650,width=650,bd=0,relief="raise")
        f4a.pack(side="right")
        f4a.configure(background="#000033")

        f4aa=Frame(f4a,height=500,width=650,bd=1,relief="raise")
        f4aa.pack(side="top")
        f4aa.configure(background="#000033")

        f4ab=Frame(f4a,height=150,width=650,bd=1,relief="raise")
        f4ab.pack(side="bottom")
        f4ab.configure(background="#000033")

        f4aaa=Frame(f4aa,height=500,width=500,bd=1,relief="raise")
        f4aaa.pack(side="left")
        f4aaa.configure(background="#000033")

        f4aab=Frame(f4aa,height=500,width=150,bd=1,relief="raise")
        f4aab.pack(side="right")
        f4aab.configure(background="#000033")

           # ======================================================================variables====================================================

        var1=IntVar()
        var1.set("0")
        var2=IntVar()
        var2.set("0")
        var3=IntVar()
        var3.set("0")
        var4=IntVar()
        var4.set("0")
        var5=IntVar()
        var5.set("0")
        var6=IntVar()
        var6.set("0")
        var7=IntVar()
        var7.set("0")
        var8=IntVar()
        var8.set("0")
        var9=IntVar()
        var9.set("0")
        var10=IntVar()
        var10.set("0")
        var11=IntVar()
        var11.set("0")

        var12=IntVar()
        var12.set("0")
        var13=IntVar()
        var13.set("0")
        var14=IntVar()
        var14.set("0")
        var15=IntVar()
        var15.set("0")
        var16=IntVar()
        var16.set("0")
        txt0=StringVar()
        txt1=StringVar()
        txt2=StringVar()
        txt3=StringVar()
        txt4=StringVar()
        txt5=StringVar()
        txt6=StringVar()
        txt7=StringVar()
        txt8=StringVar()
        txt9=StringVar()
        txt10=StringVar()
        txt11=StringVar()
        txt12=StringVar()
        txt13=StringVar()
        txt14=StringVar()
        txt15=StringVar()
        t1=StringVar()
        t2=StringVar()
        t3=StringVar()
        tv1=StringVar()
        tv2=StringVar()
        tv3=StringVar()
        t1.set("")
        t2.set("")
        t3.set("")
        txt0.set("0")
        txt1.set("0")
        txt2.set("0")
        txt3.set("0")
        txt4.set("0")
        txt5.set("0")
        txt6.set("0")
        txt7.set("0")
        txt8.set("0")
        txt9.set("0")
        txt10.set("0")
        txt11.set("0")
        txt12.set("0")
        txt13.set("0")
        txt14.set("0")
        txt15.set("0")

        DateofOrder=StringVar()
        Receipt_Ref=StringVar()
        Amount=StringVar()
        Service_Tax=StringVar()
        GST=StringVar()
        Total=StringVar()

                 

        DateofOrder.set(time.strftime("%d/%m/%y"))



            #======================================================== end of arrangement====================================================
            # ====================================================CANTEEN MANAGEMENT LABEL==================================================
        l1=Label(f2,width='1350',height='2',font=("arial",20,"bold"),text="CANTEEN MANAGEMENT",relief='solid',bg="#D3566C",fg="white") 
        l1.pack()
            # ===================================================== methods=================================================================
        def equit():
                equit=messagebox.askyesno("EXIT","Do You Want To Exit?")
                if equit>0:
                    top.destroy()
                    return

        def reset():
                fastfood()
                bevrage()
               
                var1.set("0")
                var2.set("0")
                var3.set("0")
                var4.set("0")
                var5.set("0")
                var6.set("0")
                var7.set("0")
                var8.set("0")
                var9.set("0")
                var10.set("0")
                var11.set("0")
                var12.set("0")
                var13.set("0")
                var14.set("0")
                var15.set("0")
                var16.set("0")
                
          
               
                txt0.set("0")
                txt1.set("0")
                txt2.set("0")
                txt3.set("0")
                txt4.set("0")
                txt5.set("0")
                txt6.set("0")
                txt7.set("0")
                txt8.set("0")
                txt9.set("0")
                txt10.set("0")
                txt11.set("0")
                txt12.set("0")
                txt13.set("0")
                txt14.set("0")
                txt15.set("0")
                tv1.set("")
                tv2.set("")
                tv3.set("")
                Amount.set("")
                Service_Tax.set("")
                GST.set("")
                Total.set("")
                txtl5.delete("1.0",END)
                
               
                  
        def paym():
                try:
                        m0=float(txt0.get())
                        m1=float(txt1.get())
                        m2=float(txt2.get())
                        m3=float(txt3.get())
                        m4=float(txt4.get())
                        m5=float(txt5.get())
                        m6=float(txt6.get())
                        m7=float(txt7.get())
                        m8=float(txt8.get())
                        m9=float(txt9.get())
                        m10=float(txt10.get())
                        m11=float(txt11.get())
                        m12=float(txt12.get())
                        m13=float(txt13.get())
                        m14=float(txt14.get())
                        m15=float(txt15.get())
                except Exception as e:
                        messagebox.showinfo("","ENTER INTEGER VALUE")
                
                else:
                       
               
                        amount=(m0*5)+(m1*20)+(m2*40)+(m3*10)+(m4*25)+(m5*30)+(m6*30)+(m7*25)+(m8*50)+(m9*60)+(m10*100)+(m11*40)+(m12*40)+(m13*60)+(m14*10)+(m15*10)
                        amo="Rs "+str('%.2f'%(amount))
                        Amount.set(amo)

                        service=amount*0.05
                        serve="Rs "+str('%.2f'%(service))
                        Service_Tax.set(serve)

                        gst=amount*0.12
                        gs="Rs "+str("%.2f"%(gst))
                        GST.set(gs)
                        
                        total=amount+service+gst
                        tot="Rs "+str("%.2f"%(total))
                        Total.set(tot)
                        global tr
                        tr=tuple
            #==========================================================personal information==========================================================    
        def frame():
                     root=Toplevel()
                     root.geometry("300x200")
                     root.title("Personal Information")
                   
                     m1=Label(root,text="Customer Name",width=14)
                     m1.place(relx=.2,rely=.15,anchor='c')
                     txtm1=Entry(root,width=24,textvariable=tv1)
                     txtm1.place(relx=.7,rely=.15,anchor='c')
                     m2=Label(root,text="Email Id\t\t",width=14)
                     m2.place(relx=.2,rely=.35,anchor='c')
                     txtm2=Entry(root,width=24,textvariable=tv2)
                     txtm2.place(relx=.7,rely=.35,anchor='c')
                     m3=Label(root,text="Phone No\t",width=14)
                     m3.place(relx=.2,rely=.55,anchor='c')
                     txtm3=Entry(root,width=24,textvariable=tv3)
                     txtm3.place(relx=.7,rely=.55,anchor='c')

                     def put():
                        put=messagebox.showinfo("INSERT","THANK YOU")
                        
                        root.withdraw()
                       
                        return receipt()    
                     def destro():
                        destro=messagebox.askyesno("EXIT"," Want to Close?")
                        if destro>0:
                            root.withdraw()
                            return

                        
                 


                     but1=Button(root,text="DONE",width=10,command=put)
                     but1.place(relx=.2,rely=.8,anchor="c")
                     but2=Button(root,text="KILL",width=10,command=destro)
                     but2.place(relx=.8,rely=.8,anchor="c")
               
            #==================================================database=======================================================
        def database():
                 
                ref=Receipt_Ref.get()
                dat=DateofOrder.get()
                
                db=pymysql.connect(user="root",password="Sparshj18@",host="localhost",port=3306,database="canteen")
                mycursor=db.cursor()
               
                
                bevrage()
                s=""
                if x1==1:
                    s+='TEA='+txt0.get()+','
                if x2==1:
                    s+='Black Tea='+txt1.get()+','
                if x3==1:
                    s+='Green Tea='+txt2.get()+','
                if x4==1:
                    s+='coffee='+txt3.get()+','
                if x5==1:
                    s+='Mountain Dew='+txt4.get()+','
                if x6==1:
                    s+='Sprite='+txt5.get()+','
                if x7==1:
                    s+='Mirinda='+txt6.get()+','
                if x8==1:
                    s+='Pepsi='+txt7.get()+','
                if x9==1:
                    s+='Noodles='+txt8.get()+','
                if x10==1:
                    s+='Pasta='+txt9.get()+','
                if x11==1:
                    s+='Pizza='+txt10.get()+','
                if x12==1:
                    s+='Sandwich='+txt11.get()+','
                if x13==1:
                    s+='Patties='+txt12.get()+','
                if x14==1:
                    s+='Burger='+txt13.get()+','
                
                if x15==1:
                    s+='samosa='+txt14.get()+','
                if x16==1:
                    s+='kachori='+txt15.get()+','
              
                
                   
                try:
                
                    mycursor.execute("INSERT INTO receipt (idreceipt,date,customername,emailID,phoneno,entry,total) VALUES('%s','%s','%s','%s','%d','%s','%f')\
                                 "%(ref,dat,tv1.get(),tv2.get(),int(tv3.get()),s,float(tr)))
                except Exception as e:
                    print(e)
                    
                print("data inserted")
                db.commit()
                db.close()
                s=""
                mail()
               
                
        def receipt():
                try:
                             paym()
                except Exception as e:
                             print(e)
                else:
                     x=random.randint(11000,65000)
                     ref=str(x)
                     Receipt_Ref.set("BILL"+ref)
                     txtl5.delete("1.0",END)
                     
                     txtl5.insert(END,"RECEIPT REF:"+Receipt_Ref.get()+"\t\t\t\t\t\t\t\tDate:"+DateofOrder.get()+"\n")
                    
                     txtl5.insert(END,"Customer Name:  "+ str(tv1.get()))
                     txtl5.insert(END,"\nEmail ID:  "+ tv2.get())
                     txtl5.insert(END,"\nPhone NO:  "+ tv3.get())
                     fastfood()
                     bevrage()
                     if x1==1:
                         txtl5.insert(END,"\n"+'Tea\t\t'+txt0.get()+'\tRs'+str(int(txt0.get())*5))
                     if x2==1:
                         txtl5.insert(END,"\n"+'Black Tea\t\t'+txt1.get()+'\tRs'+str(int(txt1.get())*20))
                     if x3==1:
                         txtl5.insert(END,"\n"+'Green Tea\t\t'+txt2.get()+'\tRs'+str(int(txt2.get())*40))
                     if x4==1:
                         txtl5.insert(END,"\n"+'Coffee\t\t'+txt3.get()+'\tRs'+str(int(txt3.get())*10))
                     if x5==1:
                         txtl5.insert(END,"\n"+'Mountain Dew\t\t'+txt4.get()+'\tRs'+str(int(txt4.get())*25))
                     if x6==1:
                         txtl5.insert(END,"\n"+'Sprite\t\t'+txt5.get()+'\tRs'+str(int(txt5.get())*30))
                     if x7==1:
                         txtl5.insert(END,"\n"+'Mirinda\t\t'+txt6.get()+'\tRs'+str(int(txt6.get())*30))
                     if x8==1:
                         txtl5.insert(END,"\n"+'Pepsi\t\t'+txt7.get()+'\tRs'+str(int(txt7.get())*25))
                     if x9==1:
                         txtl5.insert(END,"\n"+'Noodles\t\t'+txt8.get()+'\tRs'+str(int(txt8.get())*50))
                     if x10==1:
                         txtl5.insert(END,"\n"+'Pasta\t\t'+txt9.get()+'\tRs'+str(int(txt9.get())*60))
                     if x11==1:
                         txtl5.insert(END,"\n"+'Pizza\t\t'+txt10.get()+'\tRs'+str(int(txt10.get())*100))
                     if x12==1:
                         txtl5.insert(END,"\n"+'Sandwich\t\t'+txt11.get()+'\tRs'+str(int(txt11.get())*40))
                     if x13==1:
                         txtl5.insert(END,"\n"+'Patties\t\t'+txt12.get()+'\tRs'+str(int(txt12.get())*40))
                     if x14==1:
                         txtl5.insert(END,"\n"+'Burger\t\t'+txt13.get()+'\tRs'+str(int(txt13.get())*60))
                     if x15==1:
                         txtl5.insert(END,"\n"+'Samosa\t\t'+txt14.get()+'\tRs'+str(int(txt14.get())*10))
                     if x16==1:
                         txtl5.insert(END,"\n"+'Kachori\t\t'+txt15.get()+'\tRs'+str(int(txt15.get())*10))
                     
                     txtl5.insert(END,"\n"+'Amount\t\t\t'+Amount.get())
                     txtl5.insert(END,"\n"+'Service Tax(5%)\t\t\t'+Service_Tax.get())
                     txtl5.insert(END,"\n"+'GST(12%)\t\t\t'+GST.get())
                     txtl5.insert(END,"\n"+'Total\t\t\t'+Total.get())
             #=====================================================bevrages===============================================================   
        def bevrage():
                    
                def check():
                    if var1.get()==1:
                        txttea.configure(state="normal")
                    elif var1.get()==0:
                        txttea.configure(state="disabled")
                        txt0.set("0")

                    if var2.get()==1:
                        txtblacktea.configure(state="normal")
                    elif var2.get()==0:
                        txtblacktea.configure(state="disabled")
                        txt1.set("0")
                    if var3.get()==1:
                        txtgreentea.configure(state="normal")
                    elif var3.get()==0:
                        txtgreentea.configure(state="disabled")
                        txt2.set("0")
                    if var4.get()==1:
                        txtcoffee.configure(state="normal")
                    elif var4.get()==0:
                        txtcoffee.configure(state="disabled")
                        txt3.set("0")
                    if var5.get()==1:
                        txtMountaindew.configure(state="normal")
                    elif var5.get()==0:
                        txtMountaindew.configure(state="disabled")
                        txt4.set("0")
                    if var6.get()==1:
                        txtSprite.configure(state="normal")
                    elif var6.get()==0:
                        txtSprite.configure(state="disabled")
                        txt5.set("0")
                    if var7.get()==1:
                        txtmirinda.configure(state="normal")
                    elif var7.get()==0:
                        txtmirinda.configure(state="disabled")
                        txt6.set("0")
                    if var8.get()==1:
                        txtpepsi.configure(state="normal")
                    elif var8.get()==0:
                        txtpepsi.configure(state="disabled")
                        txt7.set("0")
                global x1
                x1=var1.get()
                global x2
                x2=var2.get()
                global x3
                x3=var3.get()
                global x4
                x4=var4.get()
                global x5
                x5=var5.get()
                global x6
                x6=var6.get()
                global x7
                x7=var7.get()
                global x8
                x8=var8.get()
                
                tea=Checkbutton(f3bba,text="Tea\t\t",variable=var1, bd=2,justify="left",width=15,onvalue=1,offvalue=0,font=("arial",10,"bold"),command=check)
                tea.place(relx=0.19,rely=0.045,anchor="c")
               
              
                txttea=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt0,state="disabled")
                txttea.place(relx=0.7,rely=0.045,anchor="c")
                
                Lab1=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 5",bg="#000033",fg="#D3566C")
                Lab1.place(relx=0.5,rely=0.045,anchor="c")
                
                
                blacktea=Checkbutton(f3bba,text="BlackTea\t",bd=2,width=15,variable=var2, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=check)
                blacktea.place(relx=0.19,rely=.1,anchor="c")
                txtblacktea=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt1,state="disabled")
                txtblacktea.place(relx=0.7,rely=0.1,anchor="c")
                Lab2=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 20",bg="#000033",fg="#D3566C")
                Lab2.place(relx=0.5,rely=0.1,anchor="c")
                
                greentea=Checkbutton(f3bba,text="Green Tea\t",bd=2,width=15,variable=var3, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=check)
                greentea.place(relx=0.19,rely=0.155,anchor="c")
                txtgreentea=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt2,state="disabled")
                txtgreentea.place(relx=0.7,rely=0.155,anchor="c")
                Lab3=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 40",bg="#000033",fg="#D3566C")
                Lab3.place(relx=0.5,rely=0.155,anchor="c")
                
                coffee=Checkbutton(f3bba,text="Coffee\t\t",bd=2,variable=var4,width=15, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=check)
                coffee.place(relx=0.19,rely=.209,anchor="c")
                txtcoffee=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt3,state="disabled")
                txtcoffee.place(relx=0.7,rely=.209,anchor="c")
                Lab4=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 10",bg="#000033",fg="#D3566C")
                Lab4.place(relx=0.5,rely=0.209,anchor="c")
                
                Mountaindew=Checkbutton(f3bba,text="Mountain Dew\t",width=15,bd=2,variable=var5, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=check)
                Mountaindew.place(relx=0.19,rely=.263,anchor="c")
                txtMountaindew=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt4,state="disabled")
                txtMountaindew.place(relx=0.7,rely=0.263,anchor="c")
                Lab5=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 25",bg="#000033",fg="#D3566C")
                Lab5.place(relx=0.5,rely=0.263,anchor="c")
                
                Sprite=Checkbutton(f3bba,text="Sprite\t\t",variable=var6,bd=2,width=15, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=check)
                Sprite.place(relx=0.19,rely=.319,anchor="c")
                txtSprite=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt5,state="disabled")
                txtSprite.place(relx=0.7,rely=0.319,anchor="c")
                Lab6=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 30",bg="#000033",fg="#D3566C")
                Lab6.place(relx=0.5,rely=0.319,anchor="c")
                
                mirinda=Checkbutton(f3bba,text="Mirinda\t\t",bd=2,variable=var7,width=15, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=check)
                mirinda.place(relx=0.19,rely=.373,anchor="c")
                txtmirinda=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt6,state="disabled")
                txtmirinda.place(relx=0.7,rely=0.373,anchor="c")
                Lab7=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 30",bg="#000033",fg="#D3566C")
                Lab7.place(relx=0.5,rely=0.373,anchor="c")
                
                pepsi=Checkbutton(f3bba,text="Pepsi\t\t",bd=2,variable=var8,width=15, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=check)
                pepsi.place(relx=0.19,rely=.427,anchor="c")
                txtpepsi=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt7,state="disabled")
                txtpepsi.place(relx=0.7,rely=0.427,anchor="c")
                Lab8=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 25",bg="#000033",fg="#D3566C")
                Lab8.place(relx=0.5,rely=0.427,anchor="c")


             
            #=================================================================fast food===============================================

        def fastfood():
                def chec():
                    if var9.get()==1:
                        txtnoodles.configure(state="normal")
                    elif var9.get()==0:
                        txtnoodles.configure(state="disabled")
                        txt8.set("0")

                    if var10.get()==1:
                        txtpasta.configure(state="normal")
                    elif var10.get()==0:
                        txtpasta.configure(state="disabled")
                        txt9.set("0")
                    if var11.get()==1:
                        txtpizza.configure(state="normal")
                    elif var11.get()==0:
                        txtpizza.configure(state="disabled")
                        txt10.set("0")
                    if var12.get()==1:
                        txtsandwich.configure(state="normal")
                    elif var12.get()==0:
                        txtsandwich.configure(state="disabled")
                        txt11.set("0")
                    if var13.get()==1:
                        txtpatties.configure(state="normal")
                    elif var13.get()==0:
                        txtpatties.configure(state="disabled")
                        txt12.set("0")
                    if var14.get()==1:
                        txtburger.configure(state="normal")
                    elif var14.get()==0:
                        txtburger.configure(state="disabled")
                        txt13.set("0")
                    if var15.get()==1:
                        txtsamosa.configure(state="normal")
                    elif var15.get()==0:
                        txtsamosa.configure(state="disabled")
                        txt14.set("0")
                    if var16.get()==1:
                        txtkachori.configure(state="normal")
                    elif var16.get()==0:
                        txtkachori.configure(state="disabled")
                        txt15.set("0")
                global x9
                x9=var9.get()
                global x10
                x10=var10.get()
                global x11
                x11=var11.get()
                global x12
                x12=var12.get()
                global x13
                x13=var13.get()
                global x14
                x14=var14.get()
                global x15
                x15=var15.get()
                global x16
                x16=var16.get()  
                noodles=Checkbutton(f3bba,text="Noodles\t\t",variable=var9, bd=2,justify="left",width=15,onvalue=1,offvalue=0,font=("arial",10,"bold"),command=chec)
                noodles.place(relx=0.19,rely=0.045,anchor="c")
                txtnoodles=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt8,state=DISABLED)
                txtnoodles.place(relx=0.7,rely=0.045,anchor="c")
                Lab9=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 50",bg="#000033",fg="#D3566C")
                Lab9.place(relx=0.5,rely=0.045,anchor="c")
                
                pasta=Checkbutton(f3bba,text="Pasta\t\t",bd=2,width=15,variable=var10, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=chec)
                pasta.place(relx=0.19,rely=.1,anchor="c")
                txtpasta=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt9,state=DISABLED)
                txtpasta.place(relx=0.7,rely=0.1,anchor="c")
                Lab10=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 60",bg="#000033",fg="#D3566C")
                Lab10.place(relx=0.5,rely=0.1,anchor="c")
                
                pizza=Checkbutton(f3bba,text="Pizza\t\t",bd=2,width=15,variable=var11, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=chec)
                pizza.place(relx=0.19,rely=0.155,anchor="c")
                txtpizza=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt10,state=DISABLED)
                txtpizza.place(relx=0.7,rely=0.155,anchor="c")
                Lab11=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 100",bg="#000033",fg="#D3566C")
                Lab11.place(relx=0.5,rely=0.155,anchor="c")
                
                sandwich=Checkbutton(f3bba,text="Sandwich\t",bd=2,variable=var12,width=15, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=chec)
                sandwich.place(relx=0.19,rely=.209,anchor="c")
                txtsandwich=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt11,state=DISABLED)
                txtsandwich.place(relx=0.7,rely=.209,anchor="c")
                Lab12=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 40",bg="#000033",fg="#D3566C")
                Lab12.place(relx=0.5,rely=0.209,anchor="c")
                
                patties=Checkbutton(f3bba,text="Patties\t\t",width=15,bd=2,variable=var13, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=chec)
                patties.place(relx=0.19,rely=.263,anchor="c")
                txtpatties=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt12,state=DISABLED)
                txtpatties.place(relx=0.7,rely=0.263,anchor="c")
                Lab13=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 40",bg="#000033",fg="#D3566C")
                Lab13.place(relx=0.5,rely=0.263,anchor="c")
                
                burger=Checkbutton(f3bba,text="Burger\t\t",variable=var14,bd=2,width=15, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=chec)
                burger.place(relx=0.19,rely=.319,anchor="c")
                txtburger=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt13,state=DISABLED)
                txtburger.place(relx=0.7,rely=0.319,anchor="c")
                Lab14=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 60",bg="#000033",fg="#D3566C")
                Lab14.place(relx=0.5,rely=0.319,anchor="c")
                
                samosa=Checkbutton(f3bba,text="Samosa\t\t",bd=2,variable=var15,width=15, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=chec)
                samosa.place(relx=0.19,rely=.373,anchor="c")
                txtsamosa=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt14,state=DISABLED)
                txtsamosa.place(relx=0.7,rely=0.373,anchor="c")
                Lab15=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 10",bg="#000033",fg="#D3566C")
                Lab15.place(relx=0.5,rely=0.373,anchor="c")
                
                kachori=Checkbutton(f3bba,text="Kachori\t\t",bd=2,variable=var16,width=15, onvalue=1,offvalue=0,font=("arial",10,"bold"),command=chec)
                kachori.place(relx=0.19,rely=.427,anchor="c")
                txtkachori=Entry(f3bba,font=("arial",10,"bold"),bd=3,justify="left", width=6,textvariable=txt15,state=DISABLED)
                txtkachori.place(relx=0.7,rely=0.427,anchor="c")
                Lab16=Label(f3bba,font=("arial",10,"bold"),bd=2,padx=25,pady=6,text="Rs 10",bg="#000033",fg="#D3566C")
                Lab16.place(relx=0.5,rely=0.427,anchor="c")
                
            #===================================================================button==================================================


        b1=Button(f3ba,text="Bevrages" ,font=("arial",12,"bold"),width=15, command=bevrage,bd=4)
        b1.place(relx=0.5, rely=0.05, anchor="c")

        b2=Button(f3ba,text="Fast Food" ,font=("arial",12,"bold"),width=15,bd=4,command=fastfood)
        b2.place(relx=0.5, rely=0.13, anchor="c")

        b3=Button(f3ba,text="North Indian" ,font=("arial",12,"bold"),width=15,bd=4)
        b3.place(relx=0.5, rely=0.21, anchor="c")
        b4=Button(f3ba,text="South Indian" ,font=("arial",12,"bold"),width=15,bd=4)
        b4.place(relx=0.5, rely=0.29, anchor="c")
        b5=Button(f3ba,text="Chineese" ,font=("arial",12,"bold"),width=15,bd=4)
        b5.place(relx=0.5, rely=0.37, anchor="c")
            #============================================================ PAYMENT ==================================================


        l1=Label(f4aab,font=("arial",12,"bold"),bd=2,padx=26,pady=8,text="PAYMENT",bg="#000033",fg="#D3566C")
        l1.place(relx=0.5,rely=0.05,anchor="c")

        i=PhotoImage(file="images/Money_50px.png")
        b6=Button(f4aab,image=i,font=("arial",12,"bold"),width=50,height=38,bd=0,command=database,bg='#000033',activebackground="#000100")
        b6.place(relx=0.5, rely=0.15, anchor="c")

        i1=PhotoImage(file="images/Card Payment_50px.png")
        b7=Button(f4aab,text="OTHER" ,image=i1,font=("arial",12,"bold"),width=50,height=35,bd=0,bg='#000033',activebackground="#000100")
        b7.place(relx=0.5, rely=0.26, anchor="c")

        l2=Label(f4aab,font=("arial",12,"bold"),padx=33,bd=3,pady=8,text="INVOICE",bg="#000033",fg="#D3566C")
        l2.place(relx=0.5,rely=0.38,anchor="c")
        i2=PhotoImage(file="images/Receipt_50px.png")

        b8=Button(f4aab,text="RECEIPT" ,image=i2,font=("arial",12,"bold"),width=50,height=49,bd=0,command=frame,bg='#000033',activebackground="#000100")
        b8.place(relx=0.5, rely=0.5, anchor="c")

        i3=PhotoImage(file="images/Reset_50px.png")
        b9=Button(f4aab,text="RESET" ,image=i3,font=("arial",12,"bold"),width=50,height=45,bd=0,command=reset,bg='#000033',activebackground="#000100")
        b9.place(relx=0.5, rely=0.63, anchor="c")

        i4=PhotoImage(file="images/Exit_50px.png")
        b10=Button(f4aab,text="EXIT" ,image=i4,font=("arial",12,"bold"),width=50,height=50,bd=0,command=equit,bg='#000033',activebackground="#000100")
        b10.place(relx=0.53, rely=0.9, anchor="c")

        i5=PhotoImage(file="images/Check_50px.png")
        b11=Button(f4aab,text="CHECK" ,image=i5,font=("arial",12,"bold"),width=50,height=45,bd=0,command=paym,bg='#000033',activebackground="#000100")
        b11.place(relx=0.5, rely=0.76, anchor="c")

            #======================================================== INFORMATION ==============================================


        l1=Label(f4ab,font=("arial",12,"bold"),bd=2,padx=25,pady=6,text="AMOUNT",bg="#000033",fg="#D3566C")
        l1.place(relx=0.1,rely=0.18,anchor="c")
        txtl1=Entry(f4ab,font=("arial",12,"bold"),bd=3,justify="left", width=17,insertwidth=2,textvariable=Amount,state=DISABLED)
        txtl1.place(relx=0.35,rely=0.18,anchor="c")
                
        l2=Label(f4ab,font=("arial",12,"bold"),bd=2,padx=8,pady=6,text="SERVICE TAX",bg="#000033",fg="#D3566C")
        l2.place(relx=0.1,rely=0.78,anchor="c")
        txtl2=Entry(f4ab,font=("arial",12,"bold"),bd=3,justify="left", width=17,insertwidth=2,textvariable=Service_Tax,state=DISABLED)
        txtl2.place(relx=0.35,rely=0.78,anchor="c")

        l3=Label(f4ab,font=("arial",12,"bold"),bd=2,padx=25,pady=6,text="GST",bg="#000033",fg="#D3566C")
        l3.place(relx=0.6,rely=0.18,anchor="c")
        txtl3=Entry(f4ab,font=("arial",12,"bold"),bd=3,justify="left", width=17,insertwidth=2,textvariable=GST,state=DISABLED)
        txtl3.place(relx=0.8,rely=0.18,anchor="c")

        l4=Label(f4ab,font=("arial",12,"bold"),bd=2,padx=25,pady=6,text="TOTAL",bg="#000033",fg="#D3566C")
        l4.place(relx=0.6,rely=0.78,anchor="c")
        txtl4=Entry(f4ab,font=("arial",12,"bold"),bd=3,justify="left", width=17,insertwidth=2,textvariable=Total,state=DISABLED)
        txtl4.place(relx=0.8,rely=0.78,anchor="c")


            #==================================================== RECEIPT======================================================


        l5=Label(f4aa,font=("arial",10,"bold"),bd=2,padx=210,pady=4,text="RECEIPT",bg="#D3566C",fg="#000033")
        l5.place(relx=0.39,rely=0.05,anchor="c")
        txtl5=Text(f4aa,font=("arial",8,"bold"),bd=2, width=78,height=30)
        txtl5.place(relx=0.39,rely=0.55,anchor="c")
        def tick():
                ti=time.strftime("%H:%M:%S")
                lab.configure(text=ti)
                lab.after(200,tick)
            #==================================================Menu==================================================
        iii1=PhotoImage(file="images/Account_50px.png")
        iii2=PhotoImage(file="images/Calendar_30px.png")
        iii3=PhotoImage(file="images/Watch_30px.png")
        ll1=Label(f3a,image=iii2,bd=0,bg="#000033",width=30)
        ll1.place(relx=.3,rely=.3,anchor="c")
        txtdate=Label(f3a,font=("arial",14,"bold"),bd=0, width=6,height=1,bg="#000033",fg="#D3566C")
        txtdate.place(relx=0.415,rely=0.3,anchor="c")
        txtdate.configure(text=DateofOrder.get())
        ll2=Label(f3a,image=iii3,bd=0,bg="#000033",width=30)
        ll2.place(relx=.3,rely=.7,anchor="c")
        lab=Label(f3a,bg="#000033",width=10,font=("Times",16,"bold"),bd=0,fg="#D3566C")
        lab.place(relx=.33,rely=.6)
        tick()

        ll3=Label(f3a,image=iii1,bd=0,bg="#000033",width=40,height=50)
        ll3.place(relx=.78,rely=.5,anchor="c")
        txtdate1=Label(f3a,text="%s"%id1,font=("Times",22,"bold"),bd=0, width=7,height=1,bg="#000033",fg="#D3566C")
        txtdate1.place(relx=0.91,rely=0.5,anchor="c")
      
        
            #==============================================history===================================================================
        iz1=PhotoImage(file="images/lines.png")
        bz1=Button(f3a,bg="#000033",bd=0,width=50,height=50,image=iz1,activebackground="#000033",command=client)
        bz1.place(relx=0.04,rely=.2)
        global v
        v=DateofOrder.get()

        top.mainloop()
#===================================================================Admin=============================================================
def admin():
        top11=Tk()
        top11.geometry("1350x750")
        top11.title("Canteen Management")
        top11.configure(background="#000011")
                
        f22=Frame(top11,height=70,width=1350,bd=1,relief="raised")
        f22.pack(side="top")
        f22.configure(background="#000033")

        f33=Frame(top11,height=650,width=1350,bd=1,relief="raised")
        f33.pack(side="bottom")
        f33.configure(background="#000033")

        f331=Frame(f33,height=80,width=1350,bd=1,relief="raised",bg="#000033")
        f331.pack(side="top")

        f332=Frame(f33,height=570,width=1350,bd=1,relief="raised",bg="#000033")
        f332.pack(side="bottom")

        l11=Label(f22,width='1350',height='2',font=("arial",26,"bold"),text="CANTEEN MANAGEMENT",relief='solid',bg="#D3566C",fg="white") 
        l11.pack()

        def tick1():
                ti=time.strftime("%H:%M:%S")
                lab.configure(text=ti)
                lab.after(200,tick1)
                

        ll11=Label(f331,text="DATE",bd=0,bg="#000033",width=30)
        ll11.place(relx=.1,rely=.5,anchor="c")
        txt1date=Label(f331,font=("arial",14,"bold"),bd=0, width=6,height=1,bg="#000033",fg="#D3566C")
        txt1date.place(relx=0.2,rely=0.5,anchor="c")
        txt1date.configure(text=v)
        ll12=Label(f331,text="TIME",bd=0,bg="#000033",width=30)
        ll12.place(relx=.4,rely=.5,anchor="c")
        la1b=Label(f331,bg="#000033",width=10,font=("Times",16,"bold"),bd=0,fg="#D3566C")
        la1b.place(relx=.5,rely=.5)
        tick1()
       
       
        top11.mainloop()

        
        
        #=========================================login========================================
def login():
        top1=Tk()
        top1.geometry("1350x750")
        top1.title("Canteen Management")
        top1.configure(background="#000033")
        x11=StringVar()
        x22=StringVar()
        x33=StringVar()
        x1=StringVar()
        x2=StringVar()
        x3=StringVar()
        y=StringVar()
        y.set("1")
        var19=IntVar()
        var19.set(1)
     
        def xz():
                y.set("0")
                l4.delete("1.0",END)
                l4.insert(END,"ADMIN")
        def x1z():
                y.set("1")
                l4.delete("1.0",END)
                l4.insert(END,"USER")
      
         
 
        def match():
              global id1
              id1=x1.get()
              db1=pymysql.connect(user="root",password="Sparshj18@",host="localhost",port=3306,database="canteen")
              mycursor1=db1.cursor()
             
              if y.get()=="1":
                    
                      try:
                           mycursor1.execute( "SELECT * FROM user")
                           res=mycursor1.fetchall()
                           for row in res:
                                f1=row[0]
                                f2=row[1]
                                f3=row[2]
                                if x1.get()==f1:
                                     if x2.get()==f2:
                                          if int(x3.get())==f3:
                                               messagebox.showinfo("info","Succeesfully Logined.")
                                               top1.withdraw()
                                               hii()
                                               
                                               
                                          else:
                                              messagebox.showinfo("","Enter correct phone number")
                                     else:
                                              messagebox.showinfo("","Enter correct password..")
                                else:
                                    messagebox.showinfo("","Enter correct username.")
                      except Exception as e:
                          print(e)
              if y.get()=="0":
                        l4.delete("1.0",END)
                        l4.insert(END,"ADMIN")
                        try:
                           mycursor1.execute( "SELECT * FROM admin")
                           res=mycursor1.fetchall()
                           for row in res:
                                f1=row[0]
                                f2=row[1]
                                f3=row[2]
                                if x1.get()==f1:
                                     if x2.get()==f2:
                                          if int(x3.get())==f3:
                                               messagebox.showinfo("info","Succeesfully Logined.")
                                               top1.withdraw()
                                               admin()
                                               
                                               
                                          else:
                                              messagebox.showinfo("","Enter correct phone number")
                                     else:
                                              messagebox.showinfo("","Enter correct password..")
                                else:
                                    messagebox.showinfo("","Enter correct username.")
                        except Exception as e:
                          print(e)
              db1.close()
        def forget():
                op1=Toplevel()
                op1.geometry("400x400+300+200")
                op1.title("client")
                op1.configure(bg="#D3566C")
                op1.resizable(False,False)
                v1=y.get()
                
                def match1():
                        x0=x11.get()
                        x01=x22.get()
                        x02=x33.get()
                        db2=pymysql.connect(user="root",password="Sparshj18@",host="localhost",port=3306,database="canteen")
                        mycurso1=db2.cursor()
                        if v1=="1":
                                mycurso1.execute("SELECT* FROM user")
                                f1=mycurso1.fetchall()
                                for row in f1:
                                        cz=row[1]
                                        if x0==cz:
                                                  if x01==x02:
                                                        mycurso1.execute("UPDATE user SET password='{}' ".format(x01))
                                                        messagebox.showinfo("","PASSWORD HAS BEEN UPDATED...")
                                                        op1.withdraw()
                                                  else:
                                                         messagebox.showinfo("","WRITTEN PASSWORD DOES NOT MATCH..")
                                        else:
                                                messagebox.showinfo("","ENTER CORRECT PASSWORD.")
                                                op1.deiconify()
                        if v1=="0":
                                mycurso1.execute("SELECT* FROM admin")
                                f1=mycurso1.fetchall()
                                for row in f1:
                                        cz=row[1]
                                        if x0==cz:
                                                  if x01==x02:
                                                        mycurso1.execute("UPDATE admin SET password='{}' ".format(x01))
                                                        messagebox.showinfo("","PASSWORD HAS BEEN UPDATED...")
                                                        op1.withdraw()
                                                  else:
                                                         messagebox.showinfo("","WRITTEN PASSWORD DOES NOT MATCH..")
                                        else:
                                                messagebox.showinfo("","ENTER CORRECT PASSWORD.")
                                                op1.deiconify()
                                
                        db2.commit()
                        db2.close()
                        x11.set("")
                        x22.set("")
                        x33.set("")
                                
                lll1=Label(op1,text="PASSWORD",font="Times 12 bold underline",bd=0,bg="#D3566C",fg="#000033")
                lll1.place(relx=0.1,rely=.1)
                tl1=Entry(op1,width=27,bg="#D3566C",fg="#000033",font="Times 18 bold",bd=1,relief="groove",textvariable=x11,show="*")
                tl1.place(relx=.5,rely=.2,anchor="c")
                lll2=Label(op1,text="NEW PASSWORD",font="Times 12 bold underline",bd=0,bg="#D3566C",fg="#000033")
                lll2.place(relx=0.1,rely=.3)
                tl2=Entry(op1,width=27,bg="#D3566C",fg="#000033",font="Times 18 bold",bd=1,relief="groove",show="*",textvariable=x22)

                tl2.place(relx=.5,rely=.4,anchor="c")
                lll3=Label(op1,text="CONFIRM  PASSWORD",font="Times 12 bold underline",bd=0,bg="#D3566C",fg="#000033")
                lll3.place(relx=0.1,rely=.5)
                lt3=Entry(op1,width=27,bg="#D3566C",fg="#000033",font="Times 18 bold",bd=1,relief="groove",textvariable=x33,show="*")

                lt3.place(relx=.5,rely=.6,anchor="c")

                lb3=Button(op1,text="UPDATE",font="Times 16 bold",bd=1,relief="groove",bg="#000033",fg="#D3566C",width=18,height=1,command=match1)
                lb3.place(relx=.5,rely=.8,anchor="c")
                
               
        f2=Frame(top1,height=70,width=1350,bd=1,relief="raise")
        f2.pack(side="top")
        f2.configure(background="#000033")

        f3=Frame(top1,height=650,width=1350,bd=1,relief="raise")
        f3.pack(side="left")
        f3.configure(background="#0E2537")


        l1=Label(f2,width='1350',height='2',font=("arial",26,"bold"),text="CANTEEN MANAGEMENT",relief='solid',bg="#D3566C",fg="white") 
        l1.pack()
        #=============================admin user  button============================
        ii1=PhotoImage(file="images/Businessman_50px.png")
        b1=Button(f3,image=ii1,width=40,height=40,bg="#0E2537",bd=0,activebackground="#000000",command=xz)
   
        b1.place(relx=.05,rely=.07,anchor="c")
        l1=Label(f3,text="Admin",font="Times 12 bold",bg="#0E2537",fg="#D3566C",bd=0,width=10)
        l1.place(relx=.05,rely=.12,anchor="c")
        ii2=PhotoImage(file="images/Account_50px.png")
        b2=Button(f3,image=ii2,width=40,height=40,bg="#0E2537",bd=0,activebackground="#000000",command=x1z )
        b2.place(relx=.1,rely=.07,anchor="c")
        l2=Label(f3,text="User",font="Times 12 bold",bg="#0E2537",fg="#D3566C",bd=0)
        l2.place(relx=.1,rely=.12,anchor="c")
        l0=Label(f3,text="-----------------------------",bg="#0E2537",fg="#D3566C",bd=0)
        l0.place(relx=.02,rely=.14)
        #============================login======================================
        lll1=Label(f3,bg="#002840",bd=0,width=60,height=4)
        lll1.place(relx=.645,rely=.145)

        lll2=Label(f3,bg="#002840",bd=0,width=60,height=2)
        lll2.place(relx=.645,rely=.74)

        l3=Label(f3,bg="#002840",bd=0,width=60,height=20)

        l3.place(relx=.8,rely=.49,anchor="c")
        l4=Text(f3,font="Times 24 bold underline",fg="#D3566C",bg="#002840",bd=0,width=10,height=1)
        l4.place(relx=.82,rely=.185,anchor="c")
        l4.insert(END,"USER")
        ll1=Label(f3,text="USERNAME",font="Times 12 bold underline",bd=0,bg="#002840",fg="#D3566C")
        ll1.place(relx=0.67,rely=.29)
        t1=Entry(f3,width=30,bg="#0E2537",fg="#D3566C",font="Times 18 bold",bd=0,relief="raised",textvariable=x1)
        t1.place(relx=.8,rely=.35,anchor="c")
        ll2=Label(f3,text="PASSWORD",font="Times 12 bold underline",bd=0,bg="#002840",fg="#D3566C")
        ll2.place(relx=0.67,rely=.40)
      
        t2=Entry(f3,width=30,bg="#0E2537",fg="#D3566C",font="Times 18 bold",bd=0,relief="raised",show="*",textvariable=x2)
        t2.place(relx=.8,rely=.46,anchor="c")
        
        ll3=Label(f3,text="PHONE NUMBER",font="Times 12 bold underline",bd=0,bg="#002840",fg="#D3566C")
        ll3.place(relx=0.67,rely=.5)
        t3=Entry(f3,width=30,bg="#0E2537",fg="#D3566C",font="Times 18 bold",bd=0,relief="raised",textvariable=x3)

        t3.place(relx=.8,rely=.56,anchor="c")

        b3=Button(f3,text="LOGIN",font="Times 16 bold",bd=0,relief="groove",bg="#0E2537",fg="#D3566C",width=18,height=1,command=match)
        b3.place(relx=.8,rely=.66,anchor="c")

        b4=Button(f3,text="Forgotten Password ?",font="Times 10 underline",bd=0,relief="groove",bg="#002840",fg="#D3566C",width=18,height=1,command=forget)
        b4.place(relx=.7,rely=.765,anchor="c")

#=======================================================Contacts us=========================================================
        xla=Label(f3,bg="#002840",bd=0,width=200,height=4)
        xla.place(relx=0,rely=.9)

        top1.mainloop()
        #==========================================================================================

if  __name__=='__main__':
        login()
       
