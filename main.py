import datetime
def gettime():
    return datetime.datetime.now()

import mysql.connector
db1 = mysql.connector.connect(host='localhost',user='root',password='KAr@2001',database='enrollment')
cur=db1.cursor()

print("Student Enrollment")
print("Hello i am BabbyBoomer \nI am here to assist you and our college SRM university which is leading universty in india"
      "i will help you to enter your personal details which will get directly to our management team \n")
print("Lets Go!!!!\n")
print("Press 0 if you want to enter your details \n OR \nPress 1 to see your personal data \nPress 2 to see full database\n")
a=int(input())
if a == 0:
    stud_id=input("enter student id")
    name=input("Enter name of student")
    age=int(input("enter age if student"))
    tenth=int(input("enter 10th class marks"))
    twelth=int(input("Enter 12th class marks"))
    date=gettime()

    s='INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s)'
    t=(stud_id,name,age,tenth,twelth,date)
    cur.execute(s,t)
    db1.commit()

elif a==1:
    name=input("Enter your name")
    my=(name,)
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='KAr@2001', port='3306', database='enrollment'
    )
    mycursor = mydb.cursor()

    mycursor.execute('SELECT * FROM students WHERE Name = %s',my)

    users1 = mycursor.fetchall()
    for user1 in users1:
        print(user1)

elif a==2:
    mydb=mysql.connector.connect(
        host='localhost',user='root',password='KAr@2001',port='3306',database='enrollment'
    )
    mycursor = mydb.cursor()

    mycursor.execute('SELECT * FROM students')
    users = mycursor.fetchall()
    for user in users:
        print(user)



