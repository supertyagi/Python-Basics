print "Factorial Finder".center(80)
num=int(input("enter any number:"))
factorial=1
if num<0:
 print "factorial does not exist for negative numbers"
elif num==0:
 print "factorial of 0 is 1"
else:
 for i in range(1,num+1):
  factorial=factorial*i
 print "the factorial of",num,"is",factorial 