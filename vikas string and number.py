def string_and_number(text, number):
    count = 0
    duplicate = number
    while duplicate!=0:
        duplicate = duplicate//10
        count+=1
    if len(text) > 10 or count > 3:
        print("Lenth of text and number should be less than 10 and 3 respectively")

    elif len(text) == 10 and count == 3:
        print(text, "" * 5, number)

    elif len(text) == 10 and count == 3:
            print(text,""*5,number)

    else:
        space = 10 - len(text)
        text = text + " "*space
        print(text," " * 3,"{0:03d}".format(number))

string_and_number("sarthak",999)



