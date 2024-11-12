###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.

#Wzór na pole powierzchni prostopadłościanu:
#A=2⋅(a⋅b+a⋅h+b⋅h)

a = int(input('a='))#zmieniamy typ zmiennej na inta, bez tego nie działało
b = int(input('b='))
c = int(input('c='))

volume = float(a*b*c)#daje float gdyby ktoś wpisał liczbę niecałkowitą

surface_area = 2 * (a * b + a * c + b * c)
print(f'powierzchnia prostopadłościanu o krawędziach {a}, {b}, {c} wynosi {surface_area}')
print(f' Objętość prostopadłościanu o krawędziach {a}, {b}, {c} wynosi {volume}')
