# Program drukuje popularne gry komputerowe w osobnych liniach, 
# numeruje listę oraz sortuje ją alfabetycznie.


computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# Sortowanie listy alfabetycznie
computer_games.sort()

# Licznik dla numerowania
i = 1

# Pętla while do drukowania
index = 0
while index < len(computer_games):
    print(f"{i}. {computer_games[index]}")  
    index += 1  # Przechodzimy do następnego indeksu
    i += 1      # Zwiększamy numer w numeracji
