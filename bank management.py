import mysql.connector as a

con = a.connect(host='localhost',
                user='root',
                passwd='Ashish12@',
                database='bank_management')

print(''' WELCOME TO BANK MANAGEMENT SYSTEM 
          USING PYTHON AND MYSQL
          ''')
print("   PROJECT BY -  ASHISH KUMAR VERMA")


def openacc():
    name = input("ENTER YOUR NAME : ")
    accno = input("ENTER YOUR ACCOUNT NUMBER : ")
    dob = input("ENTER YOUR DATE OF BIRTH : ")
    address = input("ENTER YOUR ADDRESS : ")
    contactno = int(input("ENTER YOUR CONTACT NUMBER : "))
    openingbalance = int(input("ENTER YOUR ACC OPENING AMOUNT : "))

    data1 = (name, accno, dob, address, contactno, openingbalance)
    data2 = (name, accno, openingbalance)
    sql1 = "insert into account values(%s,%s,%s,%s,%s,%s)"
    sql2 = "insert into amount values(%s,%s,%s)"
    c = con.cursor()
    c.execute(sql1, data1)
    c.execute(sql2, data2)
    con.commit()
    print("ENTERED DATA SUCCESFULLY ")
    main()


def deposit():
    am = int(input("ENTER AMOUNT : "))
    accno = input("ENTER YOUR ACCOUNT NUMBER : ")
    a = "select balance from amount where accno=%s"
    data = (accno,)
    c = con.cursor()
    c.execute(a, data)
    result = c.fetchone()
    total = result[0] + am
    sql = "update amount set balance =%s where accno =%s"
    d = (total, accno)
    c.execute(sql, d)
    con.commit()
    main()


def withdraw():
    am = int(input("ENTER AMOUNT : "))
    accno = input("ENTER YOUR ACCOUNT NUMBER : ")
    a = "select balance from amount where accno=%s"
    data = (accno,)
    c = con.cursor()
    c.execute(a, data)
    result = c.fetchone()
    total = result[0] - am
    sql = "update amount set balance =%s where accno =%s"
    d = (total, accno)
    c.execute(sql, d)
    con.commit()
    main()


def balance():
    accno = input("ENTER YOUR ACCOUNT NUMBER : ")
    a = "select balance from amount where accno=%s"
    data = (accno,)
    c = con.cursor()
    c.execute(a, data)
    result = c.fetchone()
    print("BALANCE FOR ACCOUNT  ", accno, "  IS  ", result[0])
    main()


def details():
    accno = input("ENTER YOUR ACCOUNT NUMBER : ")
    a = "select * from account where accno=%s"
    data = (accno,)
    c = con.cursor()
    c.execute(a, data)
    result = c.fetchone()
    for i in result:
        print(i, end="  ")

    main()


def closeacc():
    accno = input("ENTER YOUR ACCOUNT NUMBER : ")
    sql1 = "delete from account where accno=%s"
    sql2 = "delete from amount where accno=%s"
    data = (accno,)
    c = con.cursor()
    c.execute(sql1, data)
    c.execute(sql2, data)
    con.commit()
    main()


def main():
    print('''
       1. OPEN NEW ACCOUNT
       2. DEPOSITE AMOUNT
       3. WITHDRAW AMOUNT
       4. BALANCE INQUARY
       5. DISPLAY COSTUMER DETAILS
       6. CLOSE AN ACCOUNT
       ''')

    choice = input("ENTER THE TASK YOU WANT TO PERFORM (0-6) -  ")
    if choice == '1':
        openacc()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        balance()
    elif choice == '5':
        details()
    elif choice == '6':
        closeacc()
    elif choice == '7':
        exit()
    else:
        print("INVALID CHOICE ")
    main()


main()
