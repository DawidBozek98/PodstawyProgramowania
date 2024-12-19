# Funkcja transponująca macierz
def transpose_matrix(m):
    # Używamy list comprehension do transponowania macierzy
    # Tworzymy nową macierz, gdzie wiersze stają się kolumnami i odwrotnie
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# Funkcja do drukowania macierzy w formacie wierszy i kolumn
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))  # Łączymy elementy wiersza w jeden ciąg i wypisujemy

# Macierze do transponowania
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix_3 = [
    [5, 6, 7, 8]
]

# Transponujemy i wypisujemy macierze
print("Original Matrix 1:")
print_matrix(matrix_1)
print("\nTransposed Matrix 1:")
print_matrix(transpose_matrix(matrix_1))

print("\nOriginal Matrix 2:")
print_matrix(matrix_2)
print("\nTransposed Matrix 2:")
print_matrix(transpose_matrix(matrix_2))

print("\nOriginal Matrix 3:")
print_matrix(matrix_3)
print("\nTransposed Matrix 3:")
print_matrix(transpose_matrix(matrix_3))
