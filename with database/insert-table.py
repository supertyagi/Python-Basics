import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="college")

mycursor = mydb.cursor()

sqlform = "Insert into faculty(name, salary, subject) values (%s, %s, %s)"

faculties = [("sushant", 20000, "java"), ("nitish", 30000, "minor project"), ("yogita", 50000, "information security"), ]

mycursor.executemany(sqlform, faculties)

mydb.commit()