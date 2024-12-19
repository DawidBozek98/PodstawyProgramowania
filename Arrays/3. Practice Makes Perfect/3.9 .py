# Definicja funkcji porównującej dwie tablice
def compare(array1, array2):
    if len(array1) != len(array2):  # Jeśli tablice mają różną długość
        return False
    for i in range(len(array1)):  # Sprawdzamy elementy tablic w tych samych indeksach
        if array1[i] != array2[i]:
            return False  # Jeżeli jakikolwiek element różni się, zwrócimy False
    return True  # Jeśli wszystkie elementy są równe, zwrócimy True

# Tablice do porównania
array1_1 = ["water", "book", "sky"]
array2_1 = ["water", "book", "sky"]

array1_2 = [True, False]
array2_2 = [True, False, True]

array1_3 = [5, 3, 1]
array2_3 = [5, 3, 1]

array1_4 = [3, 2, 1]
array2_4 = [3, 2]

# Porównanie tablic i wypisanie wyników
def print_comparison_result(array1, array2):
    print("Array1:", " ".join(map(str, array1)))
    print("Array2:", " ".join(map(str, array2)))
    if compare(array1, array2):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are different")
    print()

# Porównanie wszystkich zestawów tablic
print_comparison_result(array1_1, array2_1)
print_comparison_result(array1_2, array2_2)
print_comparison_result(array1_3, array2_3)
print_comparison_result(array1_4, array2_4)
