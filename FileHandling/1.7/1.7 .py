
def read_from_file(name):
    # Otwiera plik i wczytuje jego zawartość
    with open(name) as file:
        content = file.read()
    return content

# Wczytuje cały plik i dzieli jego zawartość na linie
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

# Oblicza całkowitą liczbę zaparkowanych samochodów
total = 0
for line in file_lines:  # Iterujemy przez każdą linię w pliku
    total += int(line)   # Dodajemy wartość jako liczbę całkowitą

print('Total cars parked:', total)
