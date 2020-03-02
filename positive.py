print "CHECK YOUR NUMBER IS +VE -VE OR ZERO".center(80)
input=float(input("Enter your number:"))
if input>0:
 print "positive"
elif input<0:
 print "negative"
elif input==0:
 print "zero"
else:
 print "no such number exist"