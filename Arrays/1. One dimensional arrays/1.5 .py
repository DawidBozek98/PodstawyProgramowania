# Tablica zawiera wartości: 1, 2, 3, 4, 5


# Tworzymy tablicę
arr = [1, 2, 3, 4, 5]

# Drukujemy początkową tablicę
print('Array:', arr)

# Odejmujemy 1 od pierwszego elementu
arr[0] = arr[0] - 1
print('Array:', arr)

# Dodajemy 4 do ostatniego elementu
arr[len(arr) - 1] = arr[len(arr) - 1] + 4
print('Array:', arr)

# Mnożymy środkowy element przez 2
middle_index = len(arr) // 2
arr[middle_index] = arr[middle_index] * 2
print('Array:', arr)
