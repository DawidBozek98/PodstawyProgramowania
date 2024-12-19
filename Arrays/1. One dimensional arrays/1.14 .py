# Funkcja sortująca za pomocą algorytmu bubble sort

def bubble_sort(arr):
    n = len(arr)  # Długość listy

    for i in range(n): # Pętla przechodząca przez całą listę

        for j in range(0, n-i-1):
            # Porównujemy sąsiednie elementy
            if arr[j] > arr[j+1]:
                # Jeśli są w złej kolejności, zamieniamy je miejscami
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Przykładowa lista do posortowania
sample_array = [64, 34, 25, 12, 22, 11, 90]

# Sortowanie listy
sorted_array = bubble_sort(sample_array)


print("Sorted array:", sorted_array)
