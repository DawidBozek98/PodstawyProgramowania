import json

# Otwórz plik JSON w trybie odczytu
with open('computer.json', 'r', encoding='utf-8') as file:
   # Załaduj dane z pliku
   data = json.load(file)

# Wypisz dane
for key, value in data.items():
   print(key, ':', value)
