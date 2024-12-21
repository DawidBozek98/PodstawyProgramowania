
def read_from_file(name):
    # Otwiera plik i wczytuje jego zawartość
    with open(name, 'r') as file:
        content = file.readlines()  # Wczytuje linie do listy
    return content

# Wczytuje cały plik
file_lines = read_from_file('pets.txt')

# Zmienna do zliczania liczby słów
total_words = 0

print("Contents of pets.txt:")
for line in file_lines:
    print(line, end='') 
    words_in_line = line.split()  # Dzieli linię na słowa
    total_words += len(words_in_line)  # Dodaje liczbę słów w tej linii

print("\n\nTotal number of words:", total_words)
