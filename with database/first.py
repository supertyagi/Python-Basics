import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234")

print(mydb)
if mydb:
    print("connection successful")

else:
    print("conncection unsuccessful")