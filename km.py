print "km to mi or mi to km".center(80)
usr_inp=input("Enter 'a' to convert km to mi or b to convert mi to km:")
if usr_inp=="a":
 km=int(input("Enter the value in km:"))
 mi=km*0.621371
 print km,"km equals to",mi,"miles"
elif usr_inp=="b":
 mi=int(input("Enter the value in mi:"))
 km=mi*1.60934
 print mi,"miles equals to",km,"km" 
else:
 print "invalid input!"