# Funkcja obliczająca n-ty element ciągu Fibonacciego

def f(n):
    # Jeśli n jest 1 lub 2, to zwróć odpowiedni wynik od razu
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Dla większych n obliczamy wartości ciągu Fibonacciego
    
    a, b = 0, 1  # Pierwszy i drugi element ciągu
    for _ in range(3, n+1):  # Zaczynamy od 3. elementu
        a, b = b, a + b  # Przesuwamy wartości i obliczamy nową 
    
    return b  # Zwracamy n-ty element ciągu

# Test
print(f(5))  
print(f(9))  
