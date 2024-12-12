# Funkcja, która sprawdza, czy wyrażenie jest palindromem

def f(palindrome):
    # Używamy funkcji join do usunięcia wszystkich znaków, które nie są literami lub cyframi
    # i konwertujemy wszystkie litery na małe litery
    cleaned_string = ''.join(char.lower() for char in palindrome if char.isalnum())

    # Sprawdzamy, czy wyrażenie jest takie samo od przodu i od tyłu
    return cleaned_string == cleaned_string[::-1]

# Testowanie funkcji
print(f("radar"))         
print(f("12-11-21"))      
print(f("book"))          # Zwróci False
