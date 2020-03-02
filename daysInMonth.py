# program to check days in month

month = int(input("enter month number : "))

if month in [1 , 3 , 5 , 7 , 8 , 10 ,12]:
    print("This month has 31 days")

elif month in [4 , 6 , 9 , 11]:
    print("This month has 30 days")

elif month in [2]:
    print("This month has 28 days in normal year and 29 days in leap year")

else:
    print("invalid month number")