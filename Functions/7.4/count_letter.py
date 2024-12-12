# Funkcja do liczenia wystąpień podanej litery w danym tekście
def count_letter(text, letter):
    return text.lower().count(letter.lower())  # Zlicza litery bez uwzględniania wielkości liter
