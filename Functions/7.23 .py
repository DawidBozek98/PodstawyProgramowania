# Funkcja sprawdzająca, czy hasło jest poprawne

def f(password):
    
    # Sprawdzamy, czy hasło ma co najmniej 6 znaków
    if len(password) < 6:
        return False
    
    # Sprawdzamy, czy wszystkie znaki w haśle są unikalne
    if len(password) != len(set(password)):  # Set usuwa duplikaty
        return False
    
    # Jeśli powyższe warunki nie zostały spełnione, hasło jest poprawne
    return True

# Testowanie
print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))
