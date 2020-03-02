         print "calculator"
print ("enter 'add' to add two numbers")
print ("enter 'subtract' to subtract two numbers")
print ("enter 'divide' to divide two numbers")
print ("enter 'multiply' to multiply two numbers")
print ("enter 'quit' to exit the program")
user_input=input(" ")
if user_input=='quit':
 quit()
elif user_input=='add':
 num1=float("enter first number")
 num2=float("enter second number")
 result=str(num1+num2)
 print ("the result is"+result)
elif user_input=='subtract':
 num1=float("enter first number")
 num2=float("enter second number")
 result=str(num1-num2)
 print ("the result is"+result)
elif user_input=='divide':
 num1=float("enter first number")
 num2=float("enter second number")
 result=str(num1/num2)
 print ("the result is"+result)
elif user_input=='multiply':
 num1=float("enter first number")
 num2=float("enter second number")
 result=str(num1*num2)
 print ("the result is"+result)
else:
 print "invalid input"


