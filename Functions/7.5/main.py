
import range_check

number = int(input("A number: "))

# Określamy zakres
x = 2
y = 15

# Używamy funkcji is_in_range, aby sprawdzić, czy liczba mieści się w zakresie
if range_check.is_in_range(number, x, y):
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")
