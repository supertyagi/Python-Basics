# program to print factorial

num = int(input("Enter the number : "))
fact = 1
while num!=0:
    fact = fact*num
    num = num-1
print(fact)
