# Tablica zawierająca imiona
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

# Wypisanie oryginalnej tablicy imion
print("Names:", end=" ")
for name in names:
    print(name, end=" ")

# Znalezienie najdłuższego imienia
longest_name = names[0]  # Zakładamy, że pierwsze imię jest najdłuższe
for name in names:
    if len(name) > len(longest_name):  # Sprawdzamy, które imię jest dłuższe
        longest_name = name

# Wypisanie najdłuższego imienia
print("\nLongest name:", longest_name)
