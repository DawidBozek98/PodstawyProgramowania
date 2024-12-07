###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = int(input('Enter number: '))

if number % 2 == 0: #sprawdzamy czy reszta z dzielenia przez 2 = 0
    print(f'{number} is even')
else:
    print(f'{number} is odd')