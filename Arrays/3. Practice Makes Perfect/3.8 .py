# Definicja funkcji, która zwraca ciąg gwiazdek o długości n
def star(n):
    return '*' * n

# Tablica zawierająca liczby
numbers = [2, 6, 4, 9, 7]

# Wypisanie wartości z tablicy w formie graficznej
for number in numbers:
    print(f"{number}: {star(number)}")
