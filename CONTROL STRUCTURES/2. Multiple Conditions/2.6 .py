# wprowadzamy liczbę z klawiatury
number = float(input("Enter a number: "))

# Sprawdzamy wprowadzoną liczbę i printujemy właściwy komentarz
if number > 0:
    print(f"Number {number} is positive")
elif number < 0:
    print(f"Number {number} is negative")
else:
    print("Number is 0")