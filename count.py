a=[1,2,3,4,5,6,7,8,9]
flag=1
count=0
b=input("enter size")
for i in range(0,b):
 a[i]==input("enter your no")
for i in range(0,b):
 if a[i]=='a':
  count=count+1
  flag=1
if flag==0:
 print "not found"
else:
 print count
