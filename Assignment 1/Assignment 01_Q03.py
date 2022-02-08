# Write a function called sphere_volume that accepts a radius as a parameter
# sphere_volume(2.0) should return roughly 33.510321638291124. 
# volume= 4/3πr^3
# Asks the user to enter the radius of a sphere.


import math

# a means radious

a = float(input("Enter the radius of a sphere: "))

#B means volume function

def B(a):
    print(4*(1/3)*(math.pi)*(a**3))

B(a)
