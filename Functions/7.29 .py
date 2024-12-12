# Funkcja oblicza silnię rekurencyjnie
def factorial(n):

    # Jeśli n wynosi 0 lub 1, zwróć 1, bo 0! = 1 i 1! = 1
    if n == 0 or n == 1:
        return 1

    # Jeśli n jest większe od 1, oblicz n * (n-1)! rekurencyjnie
    if n > 1:
        return n * factorial(n - 1)

# Obliczamy silnię dla n = 5
result = factorial(5)


print("The factorial of 5 is:", result)
