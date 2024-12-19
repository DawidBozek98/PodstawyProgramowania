# Funkcja tworzy dwuwymiarową tablicę wypełnioną zerami
def create_2d_arr(x, y):
    arr = []  # Pusta lista na tablicę

    for i in range(x):  # Dla każdego wiersza

        row = []  # Pusta lista na wiersz

        for j in range(y):  # Dla każdej kolumny

            row.append(0)  # Dodanie zera do wiersza

        arr.append(row)  # Dodanie wiersza do tablicy

    return arr  # Zwrócenie 

# tablica 3x5
array = create_2d_arr(3, 5)


print("Tablica:")
for r in array:  # Wyświetlanie każdego wiersza
    print(r)
