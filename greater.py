print "CHECK WHICH NUMBER IS GREATER".center(80)
a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=float(input("enter the third number:"))
if a>b and a>c:
 print a,"is greatest"
elif b>a and b>c:
 print b,"is greatest"
elif c>a and c>b:
 print c,"is greatest"
else:
 print "all are equal"
					