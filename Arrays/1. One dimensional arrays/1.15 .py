# Funkcja bubble sort
def bubble_sort(arr):
    n = len(arr)  # Długość listy
    for i in range(n):
        # Pętla do porównania wszystkich elementów
        for j in range(0, n-i-1):
            # Porównanie sąsiednich elementów
            if arr[j] > arr[j+1]:
                # Zamiana miejscami
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Kolekcja danych - zużycie paliwa samochodów
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print("Original car fuel consumption:", car_fuel_consumption)
# Sortowanie kolekcji zużycia paliwa
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print("Sorted car fuel consumption:", sorted_car_fuel_consumption)

# Kolekcja danych - transakcje bankowe
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print("Original bank transactions:", bank_transactions)
# Sortowanie transakcji bankowych
sorted_bank_transactions = bubble_sort(bank_transactions)
print("Sorted bank transactions:", sorted_bank_transactions)
