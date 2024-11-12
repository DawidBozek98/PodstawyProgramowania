#3.1
company = "ABC Data" #nazwa: String, wartość: "ABC DATA", Typ wartości: String
phone = "555-123-009" #nazwa String, wartość: "555-123-009", Typ wartości: String
employees = 25 #nazwa: int, watrość 25, Typ wartości: int
remote_work = True #nazwa boolean, wartość: True, Typ wartości:boolean
big_company = employees > 100 # nazwa bool, wartość: False Typ wartości bool
income = 4500000 #nazwa int, wartość: 4500000, typ wartości int
income_per_person = income / employees #nazwa float, wartość income / employees, typ wartości float
print(type(company))
print(type(phone))
print(type(employees))
print(type(remote_work))
print(type(big_company))
print(type(income))
print(type(income_per_person))

# 2 * int, 2 * String, 2 * boolean, 1 * float

# 3.2 

number1 = 71
number2 = 14
number3 = 33
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)

#3.3

###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)
z = x
x = y
y = z

#używamy zmiennej 'z' jako tymczasowego nośnika danych 
#'z' przybiera wartość x
# wyzerowane 'x' przybiera wartość 'y'
#wyzerowane 'y' przybiera wartość 'z'

print("After swapping: x=", x, "y=", y)


#3.4

###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = speed_kmh/3.6
#przypisujemy zmienną speed_kmh do m/s i dzielimy przez 3.6, gdyż 1m/s to 3.6 km/h


print(speed_kmh, "km/h = ", round(speed_ms, 2), "m/s")


#3.5

###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math #importujemy klasę math
a = 5
b = 10
 #
 # Obliczanie przekątnej za pomocą wzoru Pitagorasa
diagonal = math.sqrt(a**2 + b**2)

print(f"Przekątna prostokąta o bokach {a} i {b} wynosi: {diagonal:}")

#3.6

#i.
import math
height = float(1.91)# wysokość obserwatora w metrach
d = 3.57 * math.sqrt(height) # wzorując się na poprzednim zadaniu importujemy moduł math aby móc wykorzystać metodę sqrt
print(f"Odległość od horyzontu z plaży {height}  wynosi: {d: .2f} km") #.2f oznacza zaokrąglenie do 2 miejsć po przecinku

height = float(21.91)
d = 3.57 * math.sqrt(height)
print(f"Odległość horyzontu z okna pokoju {height} wynosi {d: .2f}")

#metry od klawiatury nie zrozumiałem

#3.7
###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere

total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south/total*100)

#3.8


###
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3 #ciąg znaków '3' zmieniamy na inta
average = math + art - music + history / 4 # muzic zmieniamy na music, math brakowało h, art było duże A
print('Average grade is', average) #Podwójny apostrof jak przy wypisywaniu w Javie hehe, literówka w average
      

