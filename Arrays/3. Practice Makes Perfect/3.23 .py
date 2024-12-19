# MyText module

# Funkcja, która zwraca liczbę słów w tekście
def word_count(text):
    words = text.split()  # Dzielimy tekst na słowa
    return len(words)  # Zwracamy liczbę słów

# Funkcja, która zwraca posortowaną tablicę słów od najdłuższego do najkrótszego
def words_from_longest(text):
    words = text.split()  # Dzielimy tekst na słowa
    return sorted(words, key=len, reverse=True)  # Sortujemy według długości słów w odwrotnej kolejności

# Funkcja, która zwraca posortowaną tablicę słów alfabetycznie
def words_alphabetically(text):
    words = text.split()  # Dzielimy tekst na słowa
    return sorted(words)  # Sortujemy alfabetycznie


text = "An apple a day keeps the doctor away"

print("Text:", text)
print("Number of words:", word_count(text))
print("Words from the longest:", ", ".join(words_from_longest(text)))
print("Words ordered alphabetically:", ", ".join(words_alphabetically(text)))
