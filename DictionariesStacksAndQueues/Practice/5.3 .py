translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}
english_word = input("Enter an English word: ").lower()

# Sprawdza, czy słowo znajduje się w słowniku
if english_word in translations:
    print(f"The translation of '{english_word}' is '{translations[english_word]}'.")
else:
    print(f"Translation for '{english_word}' is unavailable.")
