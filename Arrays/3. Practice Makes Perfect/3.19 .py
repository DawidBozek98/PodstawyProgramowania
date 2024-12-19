# Program, który zlicza ile elementów w tablicy jest większych od podanej wartości

# Funkcja, która zlicza elementy większe od podanej wartości
def count_greater_than(arr, value):
    count = 0
    # Przechodzimy przez każdy element tablicy
    for num in arr:
        if num > value:  # Jeśli element jest większy od wartości
            count += 1    # Zwiększamy licznik
    return count

# Tablica rzeczywistych liczb
numbers = [12.5, 7.3, 8.9, 5.2, 19.6, 3.4]


value = float(input("Enter a value: "))


result = count_greater_than(numbers, value)
print(f"Number of elements greater than {value}: {result}")
