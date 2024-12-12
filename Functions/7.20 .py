# Funkcja, która zwraca n-ty liczby pierwszej
def f(n):

    # Licznik 
    prime_count = 0
    # Liczba, która będzie sprawdzana, czy jest liczbą pierwszą
    number = 2

    # Dopóki nie znajdziemy n-tej liczby pierwszej
    while prime_count < n:
        # Sprawdzamy, czy liczba 'number' jest liczbą pierwszą
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):  # Sprawdzamy dzielniki od 2 do pierwiastka z liczby
            if number % i == 0:  # Jeśli liczba jest podzielna przez 'i', to nie jest liczbą pierwszą
                is_prime = False
                break

        # Jeśli liczba jest pierwsza, inkrementujemy licznik
        if is_prime:
            prime_count += 1
            if prime_count == n:
                return number  # Zwracamy n-tą 

        # Zwiększamy liczbę do następnej
        number += 1

# Testowanie 
print(f(1))  
print(f(5))  
print(f(10)) 
