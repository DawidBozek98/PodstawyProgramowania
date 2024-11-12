import random
#Dice rolled: 4
#Special number (1 or 6): False

dice_roll = random.randint(1,6) #na podstawie 7.8
is_specjal_number = dice_roll == 1 or dice_roll == 6
print(f'Dice rolled: {dice_roll}')
print(f'Special number (1 or 6): {is_specjal_number}')
