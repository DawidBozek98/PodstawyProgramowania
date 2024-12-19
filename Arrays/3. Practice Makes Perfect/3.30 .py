# Tworzenie pustej tablicy 5x5
array = [[0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0]]

# Wypełnianie tablicy tabliczką mnożenia

for i in range(5):  # Pętla dla wierszy
    for j in range(5):  # Pętla dla kolumn
        array[i][j] = (i + 1) * (j + 1)  # Obliczanie wartości


for row in array:  # Dla każdego wiersza
    print(row)  
