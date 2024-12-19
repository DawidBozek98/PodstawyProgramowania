# Program sprawdzający, czy pierwsza tablica jest podzbiorem drugiej
# Oznacza to, że wszystkie elementy pierwszej tablicy muszą występować w drugiej tablicy

# Funkcja sprawdzająca, czy arr1 jest podzbiorem arr2
def is_subset(arr1, arr2):
    # Iterujemy przez każdy element pierwszej tablicy
    for element in arr1:
        # Sprawdzamy, czy dany element występuje w drugiej tablicy
        if element not in arr2:
            return False  # Jeśli jakiegoś elementu nie ma w arr2, zwracamy False
    return True  # Jeśli wszystkie elementy arr1 są w arr2, zwracamy True

# Przykładowe tablice
arr1 = [1, 3, 5]
arr2 = [1, 2, 3, 4, 5, 6]

# Sprawdzamy, czy arr1 jest podzbiorem arr2
result = is_subset(arr1, arr2)


if result:
    print("The first array is a subset of the second array.")
else:
    print("The first array is not a subset of the second array.")
