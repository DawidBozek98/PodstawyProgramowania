# Funkcja przyjmuje tekst i oddziela każdą literę znakiem "-"

def f(text):
    if text == "":  # Sprawdzamy, czy tekst jest pusty
        return ""  # Jeśli jest pusty, zwracamy pusty ciąg znaków
    else:
        return "-".join(text)  # Łączymy wszystkie litery znakiem "-", zwracamy wynik

# Testowanie
print(f("University")) 
print(f("UE")) 
print(f("x")) 
print(f(""))
