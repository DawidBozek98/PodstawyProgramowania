# Tablica zawierająca liczby naturalne
numbers = [15, 8, 31, 47, 2, 19]

# Wypisujemy zawartość tablicy w oryginalnej kolejności
print("existed array:", end=" ")
for num in numbers:
    print(num, end=" ")


print("\nreverse array:", end=" ")
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i], end=" ")
