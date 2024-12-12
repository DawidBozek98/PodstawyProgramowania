# Funkcja zwraca liczbę ujemnych liczb parzystych w przedziale <x, y>
def f(x, y):
    """
    x: początek zakresu (włącznie)
    y: koniec zakresu (włącznie)
    Zwraca: liczbę ujemnych liczb parzystych w przedziale <x, y>
    """
    count = 0  # Licznik dla ujemnych liczb parzystych
    for n in range(x, y + 1):  # Iterujemy po wszystkich liczbach
        if n < 0 and n % 2 == 0:  # Sprawdzamy, czy liczba jest ujemna i parzysta
            count += 1  # Zwiększamy licznik
    return count  
