# program to check prime number

num = int(input("Enter the number : "))
fact = 0

for i in range(2,num):
    if num%i==0:
        fact = 0
        break
    else:
        fact=1
        break
if fact==1:
    print("prime")
else:
    print("not prime")