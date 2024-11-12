print('6.1')
print()
#6.1

###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Dawid'   # replace Anna with your name
surname = 'Bożek' # replace May with your surname
characters_in_name = len(name)

full_name = name + " " + surname

print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters ')
print(f'Your full name has {len(full_name)}') # with a space between name and surname

print('6.2')
print()
#6.2

###
# A program that prints your initials
#
name = 'Dawid'
surname = 'Bozek'
print(name[0] + surname[0])
print('6.3')
print()

#6.3
###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
print(university[0:7:21] + university[7] + university[21])
print('6.4')
print()


#6.4
#In Python, to read a range of characters from the string, 
###
# A program for printing detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[21:]}')
print(f'Initials: {employee[4] + employee[9]}')

print('6.5')
print()

###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
first_group = phone[:3]#wycinamy po kolei cyfry 0-2
second_group = phone[3:6]
third_group = phone[6:]
print(f'Numer telefonu: {first_group}-{second_group}-{third_group}') 
#do testu 543097329

print('6.6')
print()
#6.6
###
# A program to print numerical representations of characters.
# a, b, z, A, B, Z, 1, =, +, €
print(f'a {ord('a')}')
print(f'b {ord('b')}')
print(f'z {ord('z')}')
print(f'A {ord('A')}')
print(f'B {ord('B')}')
print(f'Z {ord('Z')}')
print(f'1 {ord('1')}')
print(f'= {ord('=')}')
print(f'+ {ord('+')}')
print(f'€ {ord('€')}')

print('6.7')
print()

#6.7

###
# A program that prints a numerical representation of each letter of your name.
#
name = 'Dawid' # replace John with your name
print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')
print(f'The letter {name[4]} has a code {ord(name[4])}')

print('6.8')
print()

#6.8

###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = abs(first_letter_code - last_letter_code) - 1
#szukałem jak to rozwiązać, funkcja abs() pozwala obliczyć wartość dodatnią różnicy
#odejmujemy 1 na końcu żeby liczyć tylko litery pomiędzy nimi

print(f'Between {first} and {last} is {number_of_letters} letters')

#do testu A D 2, B M 10, K K 0









