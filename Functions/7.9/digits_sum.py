# Funkcja obliczająca sumę cyfr liczby w zależności od parzystości
def f(number, even):

    # Konwertujemy liczbę na ciąg znaków, żeby iterować po cyfrach
    digits = [int(digit) for digit in str(number)]
    
    # Filtrujemy cyfry w zależności od wartości parametru `even`
    if even:
        # Suma parzystych cyfr
        return sum(digit for digit in digits if digit % 2 == 0)
    else:
        # Suma nieparzystych cyfr
        return sum(digit for digit in digits if digit % 2 != 0)
