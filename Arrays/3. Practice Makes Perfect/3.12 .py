# Program, który wypisuje unikalne elementy z tablicy

# Zdefiniowana tablica
arr = [2, 3, 2, 5, 8, 1, 9, 8]

# Tworzymy pustą listę, która będzie przechowywać unikalne elementy
unique_elements = []

# Przechodzimy po tablicy
for num in arr:
    # Sprawdzamy, czy liczba występuje tylko raz w tablicy
    if arr.count(num) == 1:
        # Jeśli liczba występuje tylko raz, dodajemy ją do listy unikalnych elementów
        unique_elements.append(num)

# Wypisujemy wynik
print("Array:", *arr)
print("Unique elements:", *unique_elements)
