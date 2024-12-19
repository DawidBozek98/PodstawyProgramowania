# Definicja dwuwymiarowej tablicy
array = [
    [7, 3, 7, 9, 0],  
    [2, 9, 0, 1, 5],  
    [3, 8, 6, 4, 7],  
    [8, 7, 1, 1, 5]   
]

# zmienna do przechowywania sumy
last_column_sum = 0

# Iteracja przez każdy wiersz w tablicy
for row in array:
    # Dodanie wartości z ostatniej kolumny (indeks -1)
    last_column_sum += row[-1]


print("Suma wartości w ostatniej kolumnie:", last_column_sum)
