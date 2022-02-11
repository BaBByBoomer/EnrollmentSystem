import datetime
def gettime():
    return datetime.datetime.now()

import pymongo

client = pymongo.MongoClient("mongodb+srv://kr6654:kartik@cluster0.61uvo.mongodb.net/test")
db= client['student_db']
col=db['student_record']


print("Student Enrollment")
print("Hello i am BabbyBoomer \nI am here to assist you and our college SRM university which is leading universty in india"
      "i will help you to enter your personal details which will get directly to our management team \n")
print("Lets Go!!!!\n")
print("Press 0 if you want to enter your details \n OR \nPress 1 to see your personal data \nPress 2 to see full database\nPress 3" 
      "to update your entry\nPress 4 to delete your records")
a=int(input())
if a == 0:
    print("You want to enter your details")
    stud_id=input("enter student id")
    name=input("Enter name of student")
    age=int(input("enter age if student"))
    tenth=int(input("enter 10th class marks"))
    twelth=int(input("Enter 12th class marks"))
    date=gettime()
    data=[
        {"student_id":stud_id, "Name":name , "age":age,"Tenth Marks":tenth , "Twelth Marks":twelth , "Time_of_enrollment":date}
    ]
    col.insert_many(data)
    print("Your data is sucessfully entered")
    print("Thank you and have a nice day")

elif a==1:
    print("You want to check your data to do that :")
    id=input("Enter your student id")

    for record in col.find({'student_id':id}):
        print(record)

    print("thank you and have a nice day")

elif a==2:
    print("SO there are your collegemates try to find them and have a great friendship")
    for record in col.find():
        print(record)
    print("Thank you and have a nice day")

elif a==3:
    print("SO , you can only update your age , tenth and twelth marks to update your name contact our team")
    id = input("Enter your student id")
    query={'student_id':id}
    n_age = input("Enter your age (write same if not want to change")
    n_tenth = input("Enter your 10th marks (write same if not want to change")
    n_twelth = input("Enter your 12th marks (write same if not want to change")
    update={"$set":{"age":n_age,"Tenth Marks":n_tenth , "Twelth Marks":n_twelth }}
    col.update_one(query,update)
    print("Your updated details are")
    for result in col.find(query):
        print(result)
    print("Your data is sucessfully changed in our database")
    print("Thank you and have a nice day")
elif a==4:
    print("We are really sad that you are leaving us")
    id = input("Enter your student id")
    query = {'student_id': id}
    col.delete_one(query)
    print("We have deleted your details from our server")
    print("Have a nice day and ALL THE BEST FOR YOUR FUTURE")




