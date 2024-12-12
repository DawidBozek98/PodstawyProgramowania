# Funkcja tworząca akronim
def f(name):
    words = name.split()  # Dzielimy tekst na słowa
    acronym = ""  # Tworzymy pusty ciąg na akronim

    for word in words:
        acronym += word[0].upper()  # Dodajemy pierwszą literę każdego słowa

    return acronym  

# Testowanie 
print(f("Internet of Things"))   
print(f("For Your Information")) 
print(f("Python")) 
