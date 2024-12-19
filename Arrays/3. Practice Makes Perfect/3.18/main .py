# main.py

import  MyArrays # Importujemy nasz moduł

# Zdefiniowana tablica
numbers = [7, 3, 8, 5, 2]

# Wypisujemy wyniki z funkcji w module MyArrays
print("Numbers:", MyArrays.array_to_string(numbers))
print("Second largest number:", MyArrays.second_largest(numbers))
print("Median:", MyArrays.median(numbers))
print("Smallest and largest number:", MyArrays.smallest_largest(numbers))
