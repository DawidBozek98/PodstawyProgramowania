import json

# Otwórz plik JSON w trybie odczytu
with open('dogs.json', 'r', encoding='utf-8') as file:
   # Załaduj dane z pliku
   data = json.load(file)

# Wypisz psy młodsze niż 5 lat
for dog in data:
   if dog["age"] < 5:
      for key, value in dog.items():
         print(key, ':', value)
      print()  # Pusta linia po każdym psie
