# Definicja dwuwymiarowej tablicy 2x4
array = [
    [1, 2, 3, 4],  
    [5, 6, 7, 8]   
]

# Wyświetlanie wartości wierszami i kolumnami
print("Tablica dwuwymiarowa:") 

for row in array:  # Iterujemy przez każdy wiersz w tablicy
    for value in row:  # Iterujemy przez każdą wartość w wierszu
        print(value, end=" ")  # Wyświetlamy wartości w jednej linii
    print()  # Po zakończeniu wiersza przechodzimy do nowej linii
