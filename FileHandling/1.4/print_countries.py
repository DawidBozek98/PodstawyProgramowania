# Otwarcie pliku countries.txt w trybie odczytu (read mode)
try:
    with open("countries.txt", "r") as file:
        # Odczytywanie każdej linii z pliku i drukowanie jej zawartości
        for line in file:
            # end="" powoduje, że print() nie dodaje dodatkowego nowego wiersza
            print(line, end="")
except FileNotFoundError:
    # Wyświetlenie komunikatu w przypadku, gdy plik nie istnieje
    print("The file 'countries.txt' was not found. Make sure it is in the same folder as this program.")
