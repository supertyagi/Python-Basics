a=int(input("enter first digit"))
b=int(input("enter second digit"))
c=int(input("enter third digit"))
if (a>b) and (a>c):
 print a,"is greater"
elif (b>a) and (b>c):
 print b,"is greater"
elif (c>a) and (c>b):
 print c,"is greater"
elif (a>b) and (b>c):
 print c,"is lowest"
elif (a>b) and (c>b):
 print b,"is lowest"
elif (b>a) and (a>c):
 print c,"is lowest"
elif (b>c) and (c>a):
 print a,"is lowest"
elif (c>b) and (b>a):
 print a,"is lowest"
elif (c>a) and (a>b):
 print b,"is lowest"
else:
 print "all are equal"
