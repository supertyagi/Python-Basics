import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="collegedb")

mycursor = mydb.cursor()

# mycursor.execute("Create table faculties(name varchar(200) ,systemid int(12),subject varchar(50), salary int(20) , sex varchar(10), role varchar (20))")

# mycursor.execute("Create table students(name varchar(200) ,systemid int(12),class varchar(50), fees int(20) , sex varchar(10), role varchar (20))")

# mycursor.execute("Create table staff(name varchar(200) ,systemid int(12), salary int(20) , sex varchar(10), role varchar (20))")

mycursor.execute("Show tables")

for tb in mycursor:
    print(tb)