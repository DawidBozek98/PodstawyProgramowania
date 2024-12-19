# Tablica zawierająca liczby
numbers = [15, 8, 31, 47, 2, 19]

# Wypisanie oryginalnej tablicy
print("Array:", end=" ")
i = 0
while i < len(numbers):
    print(numbers[i], end=" ")
    i += 1

# Obliczenie sumy elementów w tablicy
sum_numbers = 0
i = 0
while i < len(numbers):
    sum_numbers += numbers[i]
    i += 1

# Obliczenie średniej arytmetycznej
mean = sum_numbers / len(numbers)


print("\nArithmetic mean:", mean)
