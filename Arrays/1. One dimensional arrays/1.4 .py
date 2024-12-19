# Tablica zawiera wartości: 2, 3, 7, 5, 4


# Tworzymy tablicę
arr = [2, 3, 7, 5, 4]

# Drukujemy całą tablicę
print(arr)

# Liczba elementów w tablicy
print('Number of elements', len(arr))

# Pierwszy element tablicy
print('First value', arr[0])

# Drugi element tablicy
print('Second value', arr[1])

# Ostatni element tablicy
print('Last value', arr[len(arr) - 1])

# Przedostatni element tablicy
print('Last but one value', arr[len(arr) - 2])

# Suma pierwszego i ostatniego elementu
print('Sum of first and last value', arr[0] + arr[len(arr) - 1])

# Środkowy element tablicy
print('Middle value', arr[len(arr) // 2])

# Wszystkie elementy tablicy oddzielone spacją (pętla)
print('All array values:')
for value in arr:
    print(value, end=' ')
