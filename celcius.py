print "convert celcius to farenheit or farenheit to celcius".center(80)
a=input("enter 'c' to convert celcius to farenheit or\n 'f' to convert farenheit to celcius:")
if a=="c":
 temp=float(input("Enter the temperature in celcius:"))
 b=temp*1.8+32
 print "the temperature in farenheit is",b
elif a=="f":
 temp=float(input("enter the temperature in farenheit:"))
 d=(temp-32)*0.5556
 print "the temperature in celcius is",d
else:
 print "the temperature is too high !"