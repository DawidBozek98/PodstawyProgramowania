#5.2

###
# A program to calculate the volume and surface area of ​​a cube.
# 

#test 
#a = 4 --> volume = 64, surface area = 96
#a = 7 --> volume = 343, surface area = 294

cube_side_string = input('Enter cube side: ') 
cube_side = int(cube_side_string) # konwersja stringa na liczbę całkowitą
cube_volume = cube_side ** 3 # obliczenie objętości a^3
cube_surface_area = 6 * (cube_side ** 2)  #pole powierzchni = 6 * a^2, nie sądziłem, że po tylu latach będę szukał tego wzoru w internecie
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_areadaw}')