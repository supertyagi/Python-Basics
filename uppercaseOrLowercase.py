# program to check lowercase or uppercase

character = str(input("Enter the Letter : "))

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
         'u', 'v', 'w', 'x', 'y', 'z']

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'
         'U', 'V', 'W', 'X', 'Y', 'Z']

if character in lower :
    print(character," is lowercase")

elif character in upper :
    print(character," is uppercase")

else:
    print("invalid character")