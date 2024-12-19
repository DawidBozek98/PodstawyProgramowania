# Funkcja bubble_sort, która sortuje tablicę
def bubble_sort(array):
    n = len(array)  # Zmienna n przechowuje długość tablicy
    # Pętla, która przechodzi przez tablicę
    for i in range(n):
        # Druga pętla, która porównuje kolejne elementy
        for j in range(0, n - i - 1):
            # Jeśli element w j-tym miejscu jest większy od następnego, zamieniamy je miejscami
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]  # Zamiana miejscami
    return array  # Zwracamy posortowaną tablicę

# Przykładowe tablice do posortowania
array1 = [64, 25, 12, 22, 11]
array2 = [5, 3, 8, 6, 2, 7]
array3 = [1, 9, 3, 5, 6, 8, 2]

# Sortowanie tablic 
print("Original array1:", array1)
sorted_array1 = bubble_sort(array1)
print("Sorted array1:", sorted_array1)

print("Original array2:", array2)
sorted_array2 = bubble_sort(array2)
print("Sorted array2:", sorted_array2)

print("Original array3:", array3)
sorted_array3 = bubble_sort(array3)
print("Sorted array3:", sorted_array3)
