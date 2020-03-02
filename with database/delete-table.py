import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="college")

mycursor = mydb.cursor()

sql = "DELETE FROM faculty WHERE name='nitish'"

mycursor.execute(sql)

mydb.commit()