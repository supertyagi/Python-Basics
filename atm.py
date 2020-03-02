am=int(input("enter your amount"))
bal=10000
if(am<=bal):
 a=am/2000
 b=am%2000
 c=b/500
 d=b%500
 e=d/100
 print "you will get",a,"two thouand rupee note",c,"five hundred rupee note",e,"hundred rupee note"
else:
 print "not enough balance"