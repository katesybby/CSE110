#extension 3
length_s = float(input("What is the length of a side of the square (in cm)? "))
ls = length_s ** 2
print (f"The area of the square is: {ls} cm^2")
print (f"The area of the square is: {ls / 10000} m^2")

length_r = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
lw = length_r * width
print (f"The area of the rectangle is: {lw} cm^2")
print (f"The area of the rectangle is: {lw / 10000} m^2")

#extension 1
import math
radius = float(input("What is the radius of the circle (in cm)? "))
area_c1 = math.pi * (radius ** 2)
print (f"The area of the circle is: {area_c1:.3f} cm^2")
print (f"The area of the circle is: {area_c1 / 10000} m^2")

#extension 2
number = float(input("input any number "))
area_s = number ** 2
area_c = math.pi * (number ** 2)
vol_c = number ** 3
vol_s = (4/3) * math.pi * (number ** 3)

print(f"area of a square: {area_s}")
print(f"area of a circle: {area_c}")
print(f"volume of cube: {vol_c}")
print(f"volume of a sphere: {vol_s}")