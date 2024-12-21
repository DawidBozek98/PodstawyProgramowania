

file_name = 'nonexistent_file.txt'

try:
    # Próbujemy otworzyć 
    file = open(file_name, 'r')  # Otwarcie w trybie odczytu
    content = file.read()  # Odczytanie zawartości 
    print(content)  # Wyświetlenie zawartości 
    file.close()  # Zamknięcie pliku 

except FileNotFoundError:
    # jeśli plik nie istnieje
    print(f"Error: The file '{file_name}' does not exist.")

