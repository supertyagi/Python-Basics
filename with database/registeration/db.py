import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234")

mycursor = mydb.cursor()

mycursor.execute("SHOW databases")

for db in mycursor:
    print(db)

