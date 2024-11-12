###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

#r = 1 --> circumference = 6.28, area = 3.14
#r = 3 --> circumference = 18.84, area = 28.26

import math

r = float(input("Enter the radius of the circle: ")) #długość promienia
pi = math.pi # wartość pi

area = pi * r * r #pi*r2
circumference = 2 * pi * r
print(f'Circle with radius {r}: ')
print(f'Circumference = {round(circumference, 2)}') #.2f nie działało szukałem innego sposobu
print(f'Area = {round(area, 2)}')