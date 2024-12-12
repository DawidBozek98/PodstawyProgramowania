# Funkcja liczy, która liczba na kostce pojawiła się najwięcej razy z rzędu

def f(dice):
    # Jeśli ciąg jest pusty, zwrócimy 0, bo nie ma żadnych rzutów

    if len(dice) == 0:
        return 0
    
    max_count = 1  # Zmienna do przechowywania największej liczby rzutów z rzędu
    current_count = 1  # Liczymy rzędy z tą samą liczbą oczek
    previous_digit = dice[0]  # Ustalamy początkowy rzut

    
    for i in range(1, len(dice)):

        # Sprawdzamy, czy obecny wynik jest taki sam jak poprzedni

        if dice[i] == previous_digit:

            current_count += 1  # Zwiększamy liczbę rzutów z rzędu
        else:
            previous_digit = dice[i]  # Zmieniamy liczbę na aktualną
            current_count = 1  # Resetujemy licznik, bo liczba się zmieniła
        
        # Sprawdzamy, czy obecna liczba rzutów z rzędu jest większa od poprzedniej maksymalnej
        if current_count > max_count:
            max_count = current_count  # Aktualizujemy maksymalną liczbę rzutów z rzędu
    
    return max_count  

# Testowanie 
print(f("5233165554211"))  
print(f("2133"))