# Tablica zawierająca liczby
numbers = [15, 8, 31, 47, 2, 19]

# Wypisanie oryginalnej tablicy
print("Array:", end=" ")
for num in numbers:
    print(num, end=" ")

# Obliczenie sumy elementów w tablicy
sum_numbers = 0
for num in numbers:
    sum_numbers += num

# Obliczenie średniej arytmetycznej
mean = sum_numbers / len(numbers)

print("\nArithmetic mean:", mean)
