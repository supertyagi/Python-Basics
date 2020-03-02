am=int(input("enter your amount"))
bal=10000
print "I don't have two thousand rupee note"
response=input("type 'c' to continue and 'e' to exit in double quotes")
if(response=="c") and (am<=bal) and (am%100==0): 
 a=am/500
 b=am%500
 f=b/100
 print "you will get",a,"five hundred rupee note",f,"hundred rupee note"
elif(am>bal):
 print "not enough balance in your account"
elif(am%100!=0):
 print "enter in the multiples of 100"
elif(response=="e"):
 quit()
