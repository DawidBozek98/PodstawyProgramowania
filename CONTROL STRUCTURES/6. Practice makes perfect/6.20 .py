# Sample result:

# Enter decimal number: 12
# 12(10) = 1100(2)


# Program do konwersji liczby dziesiętnej na liczbę binarną

decimal_number = int(input("Enter decimal number: "))

binary_number = "" # Zmienna przechowująca wynik w postaci binarnej

# Pętla, która dzieli liczbę przez 2 i zapisuje reszty
while decimal_number > 0:
    remainder = decimal_number % 2  
    binary_number = str(remainder) + binary_number  # Dodajemy resztę do przodu łańcucha
    decimal_number = decimal_number // 2  # Dzielimy liczbę przez 2 

# Wyświetlamy wynik
print(f"Binary number: {binary_number}")
