# Program, który oddziela liczby parzyste i nieparzyste w tablicy
# Liczby parzyste są umieszczane na początku, a nieparzyste na końcu

# Funkcja do oddzielania liczb parzystych i nieparzystych
def separate_even_odd(arr):
    even_numbers = []  # Lista na liczby parzyste
    odd_numbers = []   # Lista na liczby nieparzyste
    
    # Przechodzimy przez tablicę i oddzielamy liczby parzyste i nieparzyste
    for num in arr:
        if num % 2 == 0:  # Liczba parzysta
            even_numbers.append(num)
        else:  # Liczba nieparzysta
            odd_numbers.append(num)
    
    # Łączymy parzyste i nieparzyste liczby
    return even_numbers + odd_numbers

# Przykładowa tablica
arr = [7, 9, 2, 4, 5, 6]

# Oddzielamy liczby parzyste i nieparzyste
arr = separate_even_odd(arr)


print("arr =", arr)
