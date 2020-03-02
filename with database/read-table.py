import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="college")

mycursor = mydb.cursor()

############### we are fetching only one value here #########################

# mycursor.execute("Select name from faculty")
#
# myresult = mycursor.fetchone()

############## we are fetching many or all values here #######################

mycursor.execute("Select * from faculty")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)