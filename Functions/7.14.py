# Definiujemy funkcję f, która wykonuje operację matematyczną na dwóch liczbach

def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2  # Dodajemy liczby
    elif operator == "-":
        return number1 - number2  # Odejmujemy liczby
    elif operator == "*":
        return number1 * number2  # Mnożymy liczby
    elif operator == "%":
        return number1 % number2  # Zwracamy resztę z dzielenia
    elif operator == "**":
        return number1 ** number2  # Potęgujemy pierwszą liczbę do potęgi drugiej
    else:
        return "Invalid operator"  # Zwracamy komunikat, jeśli operator nie jest poprawny
    
    # Testowanie funkcji

print(f(2, 3, "+"))  
print(f(2, 3, "-"))  
print(f(2, 3, "*"))  
print(f(2, 3, "%"))  
print(f(2, 3, "**"))

