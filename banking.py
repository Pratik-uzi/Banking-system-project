import mysql.connector as my
import random as r

#============================= OPTIONS ======================================
def selection():
    print("================================================")
    print("\t\t WELCOME TO BANKING APPLICATION ")
    print()
    print("\t[1] Create Account ")
    print("\t[2] Deposit ")
    print("\t[3] Withdraw ")
    print("\t[4] Check Individual Details")
    print("\t[5] Check Master ")
    print("------------------------------------------------")
    ch=int(input("Type the choice [1-5]: "))
    if ch==1:
        create_acc()
    elif ch==2:
        deposit()
    elif ch==3:
        withdraw()
    elif ch==4:
        check_individual()
    elif ch==5:
        check_master()
    else:
        print("\t\t Please check your input...")

#============================= CREATE ACCOUNT ======================================
def create_acc():
    print()
    print("Creating New Account")
    print("=====================")
    try:
        con=my.connect(host='localhost',user='root',password='class',database='banking_pratik')
        my_cursor=con.cursor()
        name=input('Enter your name: ')
        fname=input("Enter your father's name: ")
        dob=input("Enter the date of birth (yyyy-mm-dd): ")
        addr=input("Enter the address: ")
        gen=input("Enter your gender (m/f): ")
        phone=input("Enter the mobile no: ")
        acno=r.randint(100,999)
        while True:
            bal=float(input('Enter the initial balance (min-1000): '))
            if(bal>=1000):
                break
        dop=input("Enter the today's date (yyyy-mm-dd): ")
        sql2="insert into acc_details values({},'{}','{}','{}','{}','{}','{}',{},'{}')".format(acno,name,fname,dob,addr,gen,phone,bal,dop)
        my_cursor.execute(sql2)
        con.commit()
        print('\n\t\t Congrats your account is created successfully')
        print('\t\t Your account number is: ',acno)
        print('\t\t Please remember the accno for any future tranasaction')
        print()
        
    except:
        print("Error: Unable to create the account")
        con.rollback()
        con.close()
    
        
#============================= DEPOSIT ======================================
def deposit():
    found=0
    lst=[]
    print()
    print("Transaction Deposit")
    print("=====================")
    try:
        con=my.connect(host='localhost',user='root',password='class',database='banking_pratik')
        my_cursor=con.cursor()
        acno=int(input("Enter the account no: "))
        sql1="select accno, name, bal from acc_details"
        my_cursor.execute(sql1)
        data=my_cursor.fetchall()

        for rec in data:
            if acno==rec[0]:
                found=1
                lst=rec
                break
        if found==0:
            print("Account number is invalid")
        else:
            print('\t\t(Name = {}, Avalilable balance= {})'.format(lst[1],lst[2]))
            print()
            dt=input("Enter the today's date (yyyy-mm-dd): ")
            dep=float(input("Enter the amount to be deposited: "))
            t_ty='Cr'
            amt=lst[2]+dep
            try:
                sql2="insert into transaction_details values({},'{}',{},'{}')".format(acno,t_ty,dep,dt)
                my_cursor.execute(sql2)
                sql3="update acc_details set bal={} where accno={}".format(amt,acno)
                my_cursor.execute(sql3)
                print('\n\t\t Transaction have done successfully')
                con.commit()
            except Exception as e:
                print(e)
                con.rollback()
    except:
        print("Error, unable to fetch data")
        con.close()
            
#============================= WITHDRAW ======================================
def withdraw():
    found=0
    lst=[]
    print()
    print("Transaction Withdraw")
    print("=====================")
    try:
        con=my.connect(host='localhost',user='root',password='class',database='banking_pratik')
        my_cursor=con.cursor()
        acno=int(input("Enter the account no: "))
        sql1="select accno, name, bal from acc_details"
        my_cursor.execute(sql1)
        data=my_cursor.fetchall()

        for rec in data:
            if acno==rec[0]:
                found=1
                lst=rec
                break
        if found==0:
            print("Account number is invalid")
        else:
            print('\t\t(Name = {}, Avalilable balance= {})'.format(lst[1],lst[2]))
            print()
            dt=input("Enter the today's date (yyyy-mm-dd): ")
            withd=float(input("Enter the amount to be withdrawn: "))
            t_ty='Dr'
            bal=lst[2]
            if withd>(bal-1000):
                print("\t\t Insufficient Balance")
            else:
                bal=bal-withd
                try:
                    sql2="insert into transaction_details values({},'{}',{},'{}')".format(acno,t_ty,withd,dt)
                    my_cursor.execute(sql2)
                    sql3="update acc_details set bal={} where accno={}".format(bal,acno)
                    my_cursor.execute(sql3)
                    print('\n\t\t Transaction have done successfully')
                    con.commit()
                except Exception as e:
                    print(e)
                    con.rollback()     
    except:
        print("Error: unable to fetch data")
        con.close()

#============================= CHECK BALANCE ======================================
def check_individual():
    found=0
    print()
    print("Individual Account Details")
    print("==========================")
    try:
        con=my.connect(host='localhost',user='root',password='class',database='banking_pratik')
        my_cursor=con.cursor()
        acno=int(input("Enter the account no: "))
        sql1="select accno,name, bal from acc_details"
        my_cursor.execute(sql1)
        data=my_cursor.fetchall()
        for rec in data:
            if acno==rec[0]:
                found=1
                lst=rec
                break
        if found==0:
            print("Account number is invalid")
        else:
            print("--------------------------")
            print("       : Options :        ")
            print("  [1] Check Balance   ")
            print("  [2] Account Statement ")
            print("--------------------------")
            print("Enter your choice [1 or 2]: ")
            opt=int(input("> "))
            if opt==1:
                print()
                print("\t Account No: ",lst[0],"Name: ",lst[1],"Balance: ",lst[2])
                print()
            elif opt==2:
                sql2="select * from transaction_details where accno={}".format(acno)
                my_cursor.execute(sql2)
                table=my_cursor.fetchall()
                if table==[]:
                    print("\t Sorry there is no transaction record")
                else:
                    print("Accno: ",acno)
                    print("Trans_type".ljust(10),"Amount".ljust(10),"Date_of_trans")
                    print("----------------------------------------------------------")
                    for r in table:
                        print(str(r[1]).ljust(10),str(r[2]).ljust(10),r[3])
                    print("----------------------------------------------------------")
            else:
                print("\t\t Please enter the option properly")
    except:
        print("Error: unable to fetch data")
        con.close()
    
#============================= CHECK MASTER ======================================
def check_master():
    print()
    print("Master Details")
    print("=====================")
    try:
        con=my.connect(host='localhost',user='root',password='class',database='banking_pratik')
        my_cursor=con.cursor()
        sql="select * from acc_details"
        my_cursor.execute(sql)
        rec=my_cursor.fetchall()
        print()
        print("ACNO".ljust(4),"Name".ljust(10),"Fat_Name".ljust(10),"Date_of_bir".ljust(11),"Address".ljust(10),"Gen\
der".ljust(6),"PhoneNo".ljust(10),"Balance".ljust(10),"Date_of_open")
        print("-"*90)
        for i in rec:
            print(str(i[0]).ljust(4),str(i[1]).ljust(10),str(i[2]).ljust(10),str(i[3]).ljust(11),str(i[4]).ljust(10),str(i[5]).ljust(6),str(i[6]).ljust(10),str(i[7]).ljust(10),i[8])
        print("-"*90)
    except:
        print("Error: unable to fetch data")
        con.close()

#============================== DRIVER SECTION ==================================
selection()
def askChoiceAgain():
    askChRun=input("\nWant to run again (y/n): ")
    while askChRun.lower()=='y':
        selection()
        askChRun=input("\nWant to run again (y/n): ")
askChoiceAgain()


