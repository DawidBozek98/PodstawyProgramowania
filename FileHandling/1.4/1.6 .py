
def read_from_file(name):
    # Otwiera plik w trybie odczytu 
    with open(name, 'r') as file:
        content = file.read()
    return content

# Wczytuje całą zawartość pliku
file_content = read_from_file('countries.txt')

# Dzieli zawartość pliku na linie i przechowuje w tablicy
file_lines = file_content.splitlines()

# Sortuje linie alfabetycznie
sorted_lines = sorted(file_lines)

# Drukuje tablice 
for line in sorted_lines:
    print(line)
