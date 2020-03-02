# program to check if a triangle is equilateral or scalene or isosceles triangle

first_side = int(input("Enter length of first side : "))

second_side = int(input("Enter length of second side : "))

third_side = int(input("Enter length of third side : "))

if first_side == second_side == third_side :
    print("It is equilateral triangle")

elif ((first_side == second_side ) and (first_side!=third_side )) or ((first_side == third_side) and (first_side!=second_side)) or ((second_side == third_side) and (second_side!= first_side)):
    print("It is isosceles triangle")

else :
    print("It is scalene triangle")