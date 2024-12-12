# Funkcja obliczająca wynik wyrażenia matematycznego

def f(expression):
    # Używamy wbudowanej funkcji eval(), która oblicza wynik wyrażenia
    # Na przykład "2+3" zwróci 5
    result = eval(expression)
    return result

# Testowanie 
print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))
