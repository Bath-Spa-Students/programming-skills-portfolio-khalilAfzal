# Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi 
#float is a value in which the value has decimals
r=float(input("Input the radius of the circle:"))
print("The area of the circle with radius" + " is: " + str(pi * r**2))
