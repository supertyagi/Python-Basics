print "CHECK LEAP YEAR".center(80)
year=int(input("Enter the year:"))
if (year%4==0):
 print year,"is a leap year"
elif (year%4!=0):
 print year,"is not a leap year"
else:
  print "not a valid year"