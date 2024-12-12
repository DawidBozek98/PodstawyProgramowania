# Funkcja obliczająca sumę cyfr w podanej liczbie

def sum_digits(number):

    # Konwersja liczby na wartość bezwzględną (obsługuje liczby ujemne)
    number = abs(number)

    # Konwersja liczby na ciąg znaków, aby można było iterować po cyfrach
    number_str = str(number)

    # Suma cyfr
    total = sum(int(digit) for digit in number_str)
    # Zwrócenie wyniku
    return total


any_number = int(input('Enter an integer number: '))

# Wywołanie funkcji i obliczenie sumy cyfr
result = sum_digits(any_number)

print(f'The sum of the digits in the number {any_number} is {result}')
