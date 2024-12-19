# Inicjalizujemy macierz 3x3 wypełnioną zerami
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Zamiana wartości na głównej przekątnej na 1
for i in range(len(matrix)):
    matrix[i][i] = 1  # Ustawiamy wartość na przekątnej na 1

# Wypisujemy zmodyfikowaną macierz
for row in matrix:
    print(' '.join(map(str, row)))  # Wypisujemy elementy wiersza oddzielone spacją
