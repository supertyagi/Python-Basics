# program to print table of a number

num = int(input("Enter the number : "))

for number in range(1,11):
    table = num*number
    print(num," *",number," =",table)