# Funkcja do obliczania wyrażeń RPN
def calculate_rpn(expression):
    stack = []  # Stos do przechowywania liczb
    for token in expression.split():  # Podziel wyrażenie na tokeny
        if token.isdigit():  # Jeśli token to liczba
            stack.append(int(token))  # Dodaj liczbę do stosu
        elif token in ('+', '-', '*', '/'):  # Jeśli token to operator
            b = stack.pop()  # Zdejmij dwie liczby ze stosu
            a = stack.pop()
            if token == '+':
                stack.append(a + b)  # Dodaj
            elif token == '-':
                stack.append(a - b)  
            elif token == '*':
                stack.append(a * b)  
            elif token == '/':
                stack.append(a / b)  
        elif token == '=':  
            return stack.pop()  # Zwróć wynik


expression = input("Wprowadź wyrażenie RPN: ")

# Oblicz wynik
result = calculate_rpn(expression)

# Wyświetl wynik
print("Wynik obliczeń:", result)

#do testu 2 3 + 4 5 + * =

# Przyda się na kolokwium z TPI !!
