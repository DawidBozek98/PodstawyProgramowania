# Słownik zawierający ICAO phonetic alphabet
icao_alphabet = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu'
}

# Funkcja, która zwraca odpowiednią nazwę ICAO dla danej litery
def letter_to_icao(letter):
    # Sprawdzamy, czy litera jest w słowniku
    return icao_alphabet.get(letter.upper(), letter)  # Jeśli nie ma w słowniku, zwracamy literę

# Wczytanie imienia od użytkownika
name = input('Enter your name: ')

# Dla każdej litery w imieniu wywołujemy funkcję letter_to_icao i drukujemy wynik
spelled_out_name = [letter_to_icao(letter) for letter in name]

# Wyświetlenie wyniku
print('The name spelled out using ICAO phonetic alphabet is:', ' '.join(spelled_out_name))
