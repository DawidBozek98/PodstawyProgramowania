
# Program do wypisania pierwszych N liczb pierwszych

# Funkcja sprawdzająca, czy liczba jest pierwsza
def is_prime(num):
    if num <= 1:
        return False  # Liczby mniejsze lub równe 1 nie są pierwsze
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Jeśli liczba dzieli się przez i, nie jest pierwsza
    return True  


N = int(input("Enter the number of prime numbers to find: "))

# Zmienna przechowująca liczbę znalezionych liczb pierwszych
prime_count = 0
current_number = 2  # Zaczynamy od 2, ponieważ jest to pierwsza liczba pierwsza

# Pętla do znalezienia pierwszych N liczb pierwszych
while prime_count < N:
    if is_prime(current_number):
        print(current_number, end=" ")  # Wypisz liczbę pierwszą
        prime_count += 1 
    current_number += 1  # Sprawdzamy następną liczbę

