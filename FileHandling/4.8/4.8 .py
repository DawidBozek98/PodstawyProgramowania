#  rozszerzenie pliku ma dokładnie 4 znaki
def check_extension(filename):
    # czy po kropce jest tekst
    if '.' in filename:
        # Rozdzielamy nazwę pliku na część przed i po kropce
        extension = filename.split('.')[-1]
        # Sprawdzamy, czy rozszerzenie ma dokładnie 4 znaki
        if len(extension) == 4:
            return True
    return False

try:
    with open('files.txt', 'r') as file:
        # Dla każdej linii w pliku
        for line in file:
            line = line.strip()  # Usuwamy zbędne białe znaki na początku i końcu
            # Sprawdzamy, czy rozszerzenie ma dokładnie 4 znaki
            if check_extension(line):
                print(line)  # Jeśli tak, wypisujemy nazwę 
except FileNotFoundError:
    print("Plik 'files.txt' nie został znaleziony. Upewnij się, że plik istnieje w tym samym katalogu.")
