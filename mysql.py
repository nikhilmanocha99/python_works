from pymysql import connect

connection = connect(host='localhost', user='root', password='1234qwerty', db='sbase')
def create():
    
    name = input("Enter your name: ")
    roll = int(input("Enter roll number: "))
    grade = input("Enter grade: ")
    city = input("Enter city: ")
    standard = int(input("Enter standard: "))
    cur = connection.cursor()
    cur.execute("insert into sbase (name, roll, grade, city, standard) values('{}', '{}', '{}', '{}', '{}')".format(name, roll, grade, city, standard))
    connection.commit()
    print("Record Inserted\n\n\n")


def display():
    pass
def edit():
    pass
def search():
    pass
def exit():
    pass
def delete():
    pass


while(True):
    print("press \n1. To create a table. \n2. To display a table. \n3. To edit the table. \n4. To delete the table. \n5. To search in the table. \n6. To exit")
    ch = int(input())
    if ch==1:
        create()
    elif ch==2:
        display()
    elif ch==3:
        edit()
    elif ch==4:
        delete()
    elif ch==5:
        search()
    elif ch==6:
        exit()
    else:
        print("invalid input")
