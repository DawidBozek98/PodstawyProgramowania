# Funkcja obliczająca minimalną liczbę monet potrzebnych do zapłaty

def f(amount_to_pay):

    coins = [5, 2, 1]
    count = 0

    # Iterujemy przez nominały od największego do najmniejszego
    for coin in coins:
        # Liczba monet danego nominału

        count += amount_to_pay // coin
        
        # Pozostała kwota do zapłaty
        amount_to_pay %= coin

    return count