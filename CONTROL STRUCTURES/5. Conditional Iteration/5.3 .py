###
# Prints a greeting
#
name = '' # inicjalizujemy zmienną jako ciąg pusty

while name == '': # dopóki nie podamy imienia ciąg nadal jest pusty, program czeka
    name = input('Enter your name: ') # wprowadzamy imię

print(f'Hello {name}') # drukujemy powitanie po wyjściu z pętli