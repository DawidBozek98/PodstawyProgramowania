import json
import os

# Ścieżka do pliku JSON
file_path = 'voting.json'

# odczyt danych z pliku JSON
def read_voting_data():
    # Sprawdzanie, czy plik istnieje
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)  # Zwróć dane z pliku
    return {}  # Zwróć pusty słownik

#zapisywanie danych do pliku JSON
def save_voting_data(voting_data):
    with open(file_path, 'w') as file:
        json.dump(voting_data, file, indent=4)  # Zapisz w formacie JSON

# Odczyt danych głosowania z pliku JSON
voting_data = read_voting_data()

person_name = input('Name of the person you are voting for: ')

# Zwiększ liczbę głosów lub dodaj osobę
if person_name in voting_data:
    voting_data[person_name] += 1  # Zwiększ głos
else:
    voting_data[person_name] = 1  # Dodaj nową osobę

# Zapisanie zaktualizowanych danych
save_voting_data(voting_data)


print(f'Votes for {person_name}: {voting_data[person_name]}')
