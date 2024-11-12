###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6) #na podstawie poprzedniej linii generujemy drugi rzut
dice_roll_3 = random.randint(1,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3 #dodajemy wszystkie trzy rzuty
print(f'Sum of dice rolled: {total}')