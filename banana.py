word=input("enter any word")
count=0
flag=0
y=len(word)
for i in range(0,y):
 if word[i]=='a':
  count=count+1
  flag=1
  print count
  
else:
 print "not found"