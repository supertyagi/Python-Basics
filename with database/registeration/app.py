import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="registeration")

mycursor = mydb.cursor()

class Signup:
    def __init__(self, name, email, password, confirmpassword):
        self.name = name
        self.email = email
        self.password = password
        self.confirmpassword = confirmpassword

    @classmethod
    def get_user_input(self):
        while 1:
            try:
                name = str(input("Enter Name: "))
                email = str(input("Enter email address: "))
                password = str(input("Enter password: "))
                confirmpassword = str(input("Enter confirm password: "))

                return self(name, email, password, confirmpassword)
            except:
                print('Invalid input!')
                continue

    def insert_details(self):
        sqlform = "Insert into user(name, emailid, password) values (%s, %s, %s)"

        users = [self.name, self.email, self.password, ]

        mycursor.execute(sqlform, users)

        print("Account created successfully")

        mydb.commit()

class login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def get_user_input(self):
        while 1:
            try:
                email = str(input("Enter email address: "))
                password = str(input("Enter password: "))

                return self(email, password)
            except:
                print('Invalid input!')
                continue

    def read_details(self):
        mycursor.execute('SELECT * FROM user WHERE emailid = %s AND password = %s', (self.email, self.password))
        account = mycursor.fetchone()
        if account:
            print('Logged In successfully ')
            print('Hello ! ',self.email)
        else:
            print('Invalid email or password')

action = str(input("Do you want to login or register ?: ")).lower()

if action == 'register':
 users = Signup.get_user_input()
 users.insert_details()

else:
    users = login.get_user_input()
    users.read_details()