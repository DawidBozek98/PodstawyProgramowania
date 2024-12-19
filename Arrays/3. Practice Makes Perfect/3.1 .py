# Tablica zawierająca liczby całkowite
numbers = [34, 7, 19, 4, 21, 8]

# Zmienna do przechowywania liczby liczb parzystych
even_count = 0

# Indeks do pętli while
index = 0

# Pętla while przechodząca po elementach tablicy
while index < len(numbers):
    # Sprawdzamy, czy liczba jest parzysta
    if numbers[index] % 2 == 0:
        even_count += 1  # Zwiększamy licznik liczb parzystych
    index += 1  # Przechodzimy do następnego elementu


print("Liczba liczb parzystych:", even_count)
