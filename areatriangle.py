print "Calculate Area of Triangle".center(80)
type=input("Enter the type of triangle:")
if type=="equilateral triangle":
 side=float(input("Enter the side of triangle:"))
 area=0.435*side*side
 print "Area of triangle is",area
elif type=="isosceles triangle":
 base=float(input("Enter The Base Of Triangle:"))
 height=float(input("Enter the Height of Triangle:"))
 area=0.5*base*height
 print "Area of triangle is",area
elif type=="scalene triangle":
 base=float(input("Enter The Base Of Triangle:"))
 height=float(input("Enter the Height of Triangle:"))
 area=0.5*base*height
 print "Area of triangle is",area


else:
 print "No such triangle is found !"