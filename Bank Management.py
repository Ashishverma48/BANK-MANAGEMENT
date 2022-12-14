import mysql.connector as a

con = a.connect(host='localhost',
                user='root',
                passwd='Ashish12@',
                database='bank')

cursor = con.cursor()
print("""                  WELCOME TO ..........
            BANK MANAGEMENT PROJECT---    USING PYTHON AND MYSQL
                   PROJECT BY .....ASHISH KUMAR VERMA""")


def openacc():
    name = input("ENTER YOUR NAME       : ")
    accno = input("ENTER ACCOUNT NUMBER  : ")
    dob = input("ENTER YOUR DATE OF BIRTH : ")
    ad = input("ENTER YOUR ADDRESS        : ")
    mo = input("ENTER YOUR MOBILE NUMBER  : ")
    ob = int(input("ENTER OPENING AMOUNT  : "))

    query = "insert into account values(%s,%s,%s,%s,%s,%s)"
    data = (name, accno, dob, ad, mo, ob)
    cursor.execute(query, data)
    con.commit()
    print("DATA SUCCESSFULLY ENTERED ")
    main()


def deposit():
    accno = input("ENTER YOUR ACCOUNT NUMBER  :  ")
    am = int(input("ENTER AMOUNT DEPOSIT       :  "))
    query = "select ob from account where accno=%s"
    data = (accno,)
    cursor.execute(query, data)
    result = cursor.fetchone()
    total = result[0] + am
    query1 = "update account set ob=%s where accno=%s"
    d = (total, accno)
    cursor.execute(query1, d)
    con.commit()
    print("DEPOSIT SUCCESSFULLY  ")
    main()


def withdraw():
    accno = input("ENTER YOUR ACCOUNT NUMBER :  ")
    am = int(input("ENTER WITHDRAW AMOUNT    :  "))

    query = "select ob from account where accno=%s"
    data = (accno,)
    cursor.execute(query, data)
    result = cursor.fetchone()
    total = result[0] - am

    sql = "update account set ob=%s where accno=%s"
    data1 = (total, accno)
    cursor.execute(sql, data1)
    con.commit()
    print("WITHDRAW SUCCESSFULLY ")
    main()


def inquery():
    accno = input("ENTER ACCOUNT NUMBER : ")
    query = "select ob from account where accno=%s"
    data = (accno,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    for i in result:
        print(accno, "BALANCE IS  ", i[0])
    main()


def details():
    accno = input("ENTER ACCOUNT NUMBER : ")
    query = "select * from account where accno=%s"
    data = (accno,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    for i in result:
        print('NAME     ', i[0])
        print('ACCNO   ', i[1])
        print('DOB    ', i[2])
        print('ADDRESS ', i[3])
        print('MOB NO. ', i[4])
        print('BALANCE ', i[5])
        print("")
    main()


def close():
    accno = input("ENTER ACCOUNT NUMBER : ")
    query = "delete from account where accno=%s"
    data = (accno,)
    cursor.execute(query, data)
    con.commit()
    print("ACCOUNT CLOSE SUCCESFULLY  ")

    main()


def exit():
    print("THANKS FOR USING BANK MANAGEMENT SYSTEM ")
    quit()


def main():
    print("""
            1. OPEN NEW ACCOUNT 
            2. DEPOSIT AMOUNT 
            3. WITHDRAW AMOUNT 
            4. BALANCE INQUERY
            5. CUSTOMER ACCOUNT DETAILS
            6. CLOSE ACCOUNT 
            7. EXIT  """)

    choice = input("ENTER THE TASK NUMBER YOU WANT TO PERFORME 1-7  : ")

    if choice == '1':
        openacc()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        inquery()
    elif choice == '5':
        details()
    elif choice == '6':
        close()
    elif choice == '7':
        exit()
    else:
        print("WRONG NUMBER PLEAS ENTER 1 - 7   ")

    main()


main()
