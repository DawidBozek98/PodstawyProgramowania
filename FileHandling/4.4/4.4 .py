# Program pokazujący 5 linii z pliku

# Otwórz plik
file_name = 'it_company.csv'

# Otwórz plik 
f = open(file_name, 'r')

# Wczytaj wszystkie linie z pliku
lines = f.readlines()

# Licznik linii
counter = 0

# Pętla 5 linii na raz
while counter < len(lines):
    print(lines[counter].strip())  # Pierwsza linia
    print(lines[counter+1].strip())  # Druga linia
    print(lines[counter+2].strip())  # Trzecia linia
    print(lines[counter+3].strip())  # Czwarta linia
    print(lines[counter+4].strip())  # Piąta linia
    
    # Czeka na enter
    input("Press Enter key to continue...")
    
    counter += 5  # kolejnych 5 linii


f.close()
