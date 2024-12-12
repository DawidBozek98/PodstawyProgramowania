# Funkcja oblicza sumę liczb naturalnych od 1 do n

def sum_natural(n):
    # Jeśli n jest 1, zwróć 1 (to jest przypadek bazowy)

    if n == 1:
        return 1
    
    # Jeśli n jest większe niż 1, dodaj n do sumy liczb mniejszych od n
    else:
        return n + sum_natural(n - 1)

# Obliczamy sumę liczb naturalnych w zakresie <1, 10>
result = sum_natural(10)


print("The sum of natural numbers from 1 to 10 is:", result)
