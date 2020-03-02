import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="collegedb")

mycursor = mydb.cursor()


class Faculty:
    def __init__(self, name, systemid, subject, salary, sex, role):
        self.name = name
        self.systemid = systemid
        self.subject = subject
        self.salary = salary
        self.sex = sex
        self.role = role

    @classmethod
    def get_user_input(self):
        while 1:
            try:
                name = str(input("Enter Name: "))
                systemid = int(input("Enter systemid: "))
                subject = str(input("Enter subject: "))
                salary = int(input("Enter salary: "))
                sex = str(input("Enter Sex: "))
                role = str(input("Enter Role: "))

                return self(name, systemid, subject, salary, sex, role)
            except:
                print('Invalid input!')
                continue

    def insert_details(self):
        sqlform = "Insert into faculties(name,systemid,subject,  salary, sex, role) values (%s, %s, %s, %s, %s, %s)"

        faculty = [self.name, self.systemid, self.subject, self.salary, self.sex, self.role, ]

        mycursor.execute(sqlform, faculty)

        print(mycursor.rowcount, "record(s) created")

        mydb.commit()

class Student:
    def __init__(self, name, systemid, Class, fees, sex, role):
        self.name = name
        self.systemid = systemid
        self.Class = Class
        self.fees = fees
        self.sex = sex
        self.role = role

    @classmethod
    def get_user_input(self):
        while 1:
            try:
                name = str(input("Enter Name: "))
                systemid = int(input("Enter systemid: "))
                Class = str(input("Enter class: "))
                fees = int(input("Enter fees: "))
                sex = str(input("Enter Sex: "))
                role = str(input("Enter Role: "))

                return self(name, systemid, Class, fees, sex, role)
            except:
                print('Invalid input!')
                continue

    def insert_details(self):
        sqlform = "Insert into students(name, systemid, Class,  fees, sex, role) values (%s, %s, %s, %s, %s, %s)"

        student = [self.name, self.systemid, self.Class, self.fees, self.sex, self.role, ]

        mycursor.execute(sqlform, student)

        print(mycursor.rowcount, "record(s) created")

        mydb.commit()

class Staff:
    def __init__(self, name, systemid, salary, sex, role):
        self.name = name
        self.systemid = systemid
        self.salary = salary
        self.sex = sex
        self.role = role

    @classmethod
    def get_user_input(self):
        while 1:
            try:
                name = str(input("Enter Name: "))
                systemid = int(input("Enter systemid: "))
                salary = int(input("Enter salary: "))
                sex = str(input("Enter Sex: "))
                role = str(input("Enter Role: "))

                return self(name, systemid, salary, sex, role)
            except:
                print('Invalid input!')
                continue

    def insert_details(self):
        sqlform = "Insert into staff(name, systemid, salary, sex, role) values (%s, %s, %s, %s, %s)"

        staffs = [self.name, self.systemid, self.salary, self.sex, self.role, ]

        mycursor.execute(sqlform, staffs)

        print(mycursor.rowcount, "record(s) created")

        mydb.commit()


def read_details():
    user_id = int(input("Enter system ID: "))
    sql = "SELECT * FROM {} WHERE systemid = %s".format(table)
    search = (user_id,)

    mycursor.execute(sql, search)

    myresult = mycursor.fetchall()

    for x in myresult:
        print("Name : ", x[0])
        print("system id : ", x[1])
        print("subject : ", x[2])
        print("salary : ", x[3])
        print("sex : ", x[4])
        print("role : ", x[5])

    print(mycursor.rowcount, "record(s) was read")

def update_details():
    field = input("Enter the field you want to change: ").lower()
    new = input("Enter the new value: ")
    systemid = int(input("Enter the systemid: "))
    sql = "UPDATE {} SET {} = %s WHERE systemid = %s".format(table, field)
    val = (new, systemid)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) updated")

def delete_details():
    systemid = int(input("Enter system id to delete record: "))
    sql = "DELETE FROM {} WHERE systemid = %s".format(table)
    user_id = (systemid,)

    mycursor.execute(sql, user_id)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

while True:
    print(" "*50)
    print("Choose a category: Faculty, student, staff or quit to exit the application")
    category = str(input("Enter category: ")).lower()
    if category == "quit":
        break
    headline = """
    Enter your choice from the following:
    Type create to create an entry
    Type read to read a detail
    Type update to update a detail
    Type delete to delete a detail
    """
    print(headline)

    choice = str(input("Enter your choice: ")).lower()

    if category == "faculty":
        table = "faculties"
        if choice == "create":
         Person = Faculty.get_user_input()
         Person.insert_details()

        elif choice == "read":
            read_details()

        elif choice == "update":
            update_details()
        else:
            delete_details()

    elif category == "student":
        table = "students"
        if choice == "create":
            Person = Student.get_user_input()
            Person.insert_details()

        elif choice == "read":
            read_details()

        elif choice == "update":
            update_details()
        else:
            delete_details()

    elif category == "staff":
        table = "staff"
        if choice == "create":
         Person = Staff.get_user_input()
         Person.insert_details()

        elif choice == "read":
            user_id = int(input("Enter system ID: "))
            sql = "SELECT * FROM {} WHERE systemid = %s".format(table)
            search = (user_id,)

            mycursor.execute(sql, search)

            myresult = mycursor.fetchall()

            for x in myresult:
                print("Name : ", x[0])
                print("system id : ", x[1])
                print("salary : ", x[2])
                print("sex : ", x[3])
                print("role : ", x[4])


        elif choice == "update":
            update_details()
        else:
            delete_details()





