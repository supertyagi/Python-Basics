# program to check if a triangle can be formed

first_side = int(input("Enter length of first side : "))

second_side = int(input("Enter length of second side : "))

third_side = int(input("Enter length of third side : "))

if (first_side + second_side > third_side) and (first_side + third_side > second_side) and (second_side + third_side > first_side) :
    print("Triangle can be formed")

else :
    print("Triangle can not be formed")