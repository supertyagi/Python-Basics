# ask the user to enter the command until x

command = str(input("Enter the command : ")).lower()

while command!="x":
    if command!="x":
        print(command)
        print("Please enter the required command")
        command = str(input("Enter the command : ")).lower()
    else :
        break
print("Required command is met")

