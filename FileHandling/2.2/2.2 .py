# Lista Siedmiu Cudów Świata
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Nazwa pliku do zapisu
file_name = 'seven_wonders.txt'

# Sortowanie danych alfabetycznie
seven_wonders.sort()

# Zapis danych do pliku
with open(file_name, 'w') as file:
    for item in seven_wonders:
        file.write(item + '\n')  # Zapis każdego elementu w nowej linii
