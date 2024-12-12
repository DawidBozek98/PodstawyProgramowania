# Funkcja oblicza sumę liczb w zakresie <x, y>, które są podzielne przez 2 i 3, ale nie przez 4

def f(x, y):
    total_sum = 0  # Tutaj przechowujemy sumę liczb
    
    # Iterujemy po liczbach w tym y
    for number in range(x, y+1):
        
        # Sprawdzamy, czy liczba jest podzielna przez 2 i 3, ale nie przez 4
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total_sum += number  # Dodajemy liczbę do sumy, jeśli spełnia warunki
            
    return total_sum  

# Testowanie
print(f(1, 20))
print(f(10, 30))
