print "is your number palindrome or not ?".center(80)
num=int(input("enter any number"))
b=0
temp=num
while(num!=0):
 a=num%10
 b=b*10+a
 num=num/10
if(b==temp):
 print num,"number is palindrome"
else:
 print "number is not palindrome" 