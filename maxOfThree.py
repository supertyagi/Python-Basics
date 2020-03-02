# to find max of three numbers

numOne = int(input("Enter first number : "))

numTwo = int(input("Enter second number : "))

numThree = int(input("Enter third number : "))

if numOne > numTwo and numOne > numThree :
    print(numOne," is greater")

elif numTwo > numOne and numTwo > numThree :
    print(numTwo," is greater")

elif numThree > numOne and numThree > numTwo :
    print(numThree," is greater")

else:
    print("all are equal")