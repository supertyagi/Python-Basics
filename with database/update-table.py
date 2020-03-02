import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="college")

mycursor = mydb.cursor()

sql = ("UPDATE faculty SET salary=70000  WHERE name='sushant' ")

mycursor.execute(sql)

mydb.commit()