import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="registeration")

mycursor = mydb.cursor()

# mycursor.execute("Create table user(name varchar(200) ,emailid varchar (50), password varchar(50))")

mycursor.execute("SHOW tables")

for tb in mycursor:
    print(tb)