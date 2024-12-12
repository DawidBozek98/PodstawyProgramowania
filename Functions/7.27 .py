# Funkcja sprawdza, czy kod produktu jest poprawny

def f(product_code):

    # Sprawdzamy, czy kod ma dokładnie 4 cyfry

    if len(product_code) == 4:

        # Pobieramy pierwsze trzy cyfry i czwórką
        first_three_digits = product_code[:3]  # Pierwsze trzy cyfry
        control_digit = int(product_code[3])  # Czwórka kontrolna
        
        # Liczymy sumę pierwszych trzech cyfr
        sum_of_digits = sum(int(digit) for digit in first_three_digits)
        
        # Liczymy resztę z dzielenia sumy przez 7
        calculated_control_digit = sum_of_digits % 7
        
        # Sprawdzamy, czy czwórka kontrolna jest równa obliczonej reszcie
        if control_digit == calculated_control_digit:
            return True 
        else:
            return False
    else:
        return False  # Jeśli kod ma inną długość niż 4, jest niepoprawny

# Testowanie 
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))
