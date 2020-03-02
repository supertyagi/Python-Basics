print "Solve the quadratic equation".center(80)
print "ax**2 + bx + c = 0 is the general form".center(80)
import cmath
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
d=(b**2)-(4*a*c)
x1=(-b+cmath.sqrt(d))/(2*a)
x2=(-b-cmath.sqrt(d))/(2*a)
print x1,"and",x2,"are the roots of the given equation"