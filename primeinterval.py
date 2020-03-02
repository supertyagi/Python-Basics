print "CHECK PRIME NUMBERS IN AN INTERVAL".center(80)
a=int(input("Enter the first value of interval:"))
b=int(input("Enter the last value of interval "))
for i in range(a,b):
 if (i%2!=0):
  print i,"are prime numbers"
else:
 print "ENTER A VALID INTERVAL".center(80)