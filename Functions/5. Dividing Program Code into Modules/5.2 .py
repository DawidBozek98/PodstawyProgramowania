def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')


# Funkcja do konwersji centymetrów na cale
def cm_to_inch(n):
    # 1 cal = 2.54 cm, więc dzielimy przez 2.54, aby uzyskać liczbę cali
    return n / 2.54

# Funkcja do konwersji stóp i cali na centymetry
def ft_inch_to_cm(feet, inches):
    # Najpierw konwertujemy stopy na cale (1 stopa = 12 cali), a potem dodajemy cale
    total_inches = (feet * 12) + inches
    # Następnie konwertujemy cale na centymetry (1 cal = 2.54 cm)
    return total_inches * 2.54


# Główna część programu do testowania wszystkich funkcji
if __name__ == "__main__":
    
    # Testowanie funkcji konwertujących
    print(f'2m = {m_to_cm(2)} cm')  
    print(f'532 cm = {cm_to_m(532)} m')  
    print(f'100 cm = {cm_to_inch(100)} inches')  
    print(f'5 feet 10 inches = {ft_inch_to_cm(5, 10)} cm')  