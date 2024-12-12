# Funkcja oblicza x do potęgi n za pomocą rekurencji

def power(x, n):
    # Przypadek bazowy: jeśli n jest 0, zwróć 1 (ponieważ x^0 = 1)

    if n == 0:
        return 1
    # Rekurencja: x^n = x * x^(n-1)

    else:
        return x * power(x, n - 1)

result = power(5, 3)

print("5 raised to the power of 3 is:", result)
