



# Pytamy użytkownika o odpowiedzi na pytania w ankiecie i zapisujemy je jako zmienne logiczne (True/False)
interested_in_computer_science = input("Are you interested in computer science? (y/n): ").strip().lower() == 'y' #.strip() oraz .lower() znalezione w internecie  strip usuwa zbędne spacje, a lower traktuje duże litery jak małe
like_playing_computer_games = input("Do you like playing computer games? (y/n): ").strip().lower() == 'y'
has_instagram_account = input("Do you have an Instagram account? (y/n): ").strip().lower() == 'y'

# Wyświetlamy wyniki ankiety
print("\nSURVEY RESULTS") # \n w nowej linii

# Wyświetlamy wyniki, zamieniając True na 'Yes', a False na 'No'
print(f"Interested in computer science: {'Yes' if interested_in_computer_science else 'No'}")
print(f"Playing computer games: {'Yes' if like_playing_computer_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if has_instagram_account else 'No'}")
