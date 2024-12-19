import random  # Importujemy bibliotekę random, aby móc losować elementy

# Definicja funkcji rand_elem, która zwraca losowo wybrany element z tablicy
def rand_elem(array):
    return random.choice(array)  # Wybieramy losowy element z tablicy

# Tablica, z której będziemy losować
arr = [10, 20, 30, 40, 50]


print(rand_elem(arr))  
print(rand_elem(arr))  
print(rand_elem(arr))  
