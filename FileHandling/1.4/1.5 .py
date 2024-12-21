# Otwarcie pliku countries.txt w trybie odczytu 
try:
    with open("countries.txt", "r") as file:
        # Inicjalizacja numeru linii
        line_number = 1
        
        # Odczytywanie każdej linii z pliku i drukowanie jej zawartości z numeracją
        for line in file:
            # Usunięcie znaków końca linii i dodanie numeracji
            print(f"{line_number}. {line.strip()}")
            
       
            line_number += 1
except FileNotFoundError:
    print("The file 'countries.txt' was not found. Make sure it is in the same folder as this program.")
