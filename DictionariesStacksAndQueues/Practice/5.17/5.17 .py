import json

# Otwórz plik JSON w trybie odczytu
with open('cities.json', 'r', encoding='utf-8') as file:
   # Załaduj dane z pliku
   data = json.load(file)

# Wypisz dane o miastach
for city in data:
   for key, value in city.items():
      print(key, ':', value)
   print()  # Pusta linia po każdym mieście
