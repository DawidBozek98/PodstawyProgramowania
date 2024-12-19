# Funkcja, która sprawdza, czy liczba występuje w tablicy
def occurs(number, array):
    # Zwraca True, jeśli liczba jest w tablicy
    return number in array

# Tablica, w której będziemy szukać liczby
arr = [15, 38, 7, 23, 14]

# Pobieramy liczbę od użytkownika
number = int(input("Number: "))

# Sprawdzamy, czy liczba jest w tablicy
if occurs(number, arr):
    print(f"Array: {' '.join(map(str, arr))}")
    print(f"Result: number {number} appears in the array")
else:
    print(f"Array: {' '.join(map(str, arr))}")
    print(f"Result: number {number} does not appear in the array")
