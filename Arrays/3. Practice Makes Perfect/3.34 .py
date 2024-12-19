# Tworzymy funkcję, która generuje macierz jednostkową
def identity_matrix(n):
    # Tworzymy pustą listę, to będzie nasza macierz
    matrix = []
    
    # Iterujemy przez wiersze
    for i in range(n):
        row = []  # Tworzymy pusty wiersz
        # Iterujemy przez kolumny
        for j in range(n):
            # Jeśli i == j, to wstawiamy 1, w przeciwnym razie 0
            if i == j:
                row.append(1)
            else:
                row.append(0)
        # Dodajemy wiersz do macierzy
        matrix.append(row)
    
    # Zwracamy macierz
    return matrix

# Funkcja, która wypisuje macierz 2D w formacie wierszy i kolumn
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))  # Łączymy elementy wiersza w jeden ciąg i wypisujemy

# Tworzymy trzy macierze jednostkowe o różnych rozmiarach
matrix_3x3 = identity_matrix(3)
matrix_5x5 = identity_matrix(5)
matrix_8x8 = identity_matrix(8)


print("3x3 Identity Matrix:")
print_matrix(matrix_3x3)

print("\n5x5 Identity Matrix:")
print_matrix(matrix_5x5)

print("\n8x8 Identity Matrix:")
print_matrix(matrix_8x8)
