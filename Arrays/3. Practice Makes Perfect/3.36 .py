# Funkcja, która spłaszcza tablicę 2D na 1D
def flatten_2d_array(arr_2d):
    result = []  # Tworzymy pustą listę, do której będziemy dodawać elementy z tablicy 2D
    for row in arr_2d:  # Przechodzimy przez każdą linię (wiersz) w tablicy 2D
        for elem in row:  # Przechodzimy przez każdy element w danym wierszu
            result.append(elem)  # Dodajemy element do nowej listy 1D
    return result  # Zwracamy wynikową tablicę 1D

# Funkcja do drukowania tablicy 1D
def print_1d_array(arr_1d):
    print(arr_1d)  # Wypisujemy całą tablicę 1D na ekran

# Nasze przykładowe tablice 2D
array_1 = [
    [2, 3],  
    [1, 5]  
]

array_2 = [
    [5, 0, 3, 7, 5],  
    [9, 0, 9, 1, 2]  
]

array_3 = [
    [2, 1],
    [3, 5],  
    [7, 4],  
    [2, 6]  
]

# Konwertowanie tablic 2D na 1D i wypisanie wyników
# Najpierw konwertujemy pierwszą tablicę, potem drukujemy wynik
print_1d_array(flatten_2d_array(array_1))  

print_1d_array(flatten_2d_array(array_2)) 

print_1d_array(flatten_2d_array(array_3))  