#5.1

# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')


#5.2

###
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_side_string = input('Enter cube side: ') 
cube_side = int(cube_side_string) # konwersja stringa na liczbę całkowitą
cube_volume = cube_side ** 3 # obliczenie objętości a^3
cube_surface_area = 6 * (cube_side ** 2)  #pole powierzchni = 6 * a^2, nie sądziłem, że po tylu latach będę szukał tego wzoru w internecie
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_areadaw}')