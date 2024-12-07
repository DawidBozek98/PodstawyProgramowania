###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input('Enter your first number: '))
number2 = float(input('Enter your second number: '))
operator = input('Enter operator: ')
result = 0 #przypisujemy wartość początkową na 0
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
else:
    operator == '/'
    result = number1 / number2


# print result
print(f'{number1} {operator} {number2} = {result}')