# Functions to read any data type from the keyboard


def input_string(message):
    return input(message)  

# Funkcja wczytująca liczbę całkowitą (integer) z klawiatury
def input_integer(message):
    return int(input(message))  

# Funkcja wczytująca liczbę zmiennoprzecinkową (real) z klawiatury
def input_real(message):
    return float(input(message))  

# Funkcja wczytująca wartość logiczną (True/False) na podstawie odpowiedzi 'y' lub 'n'
def input_boolean(message):
    return input(message).strip().lower() == 'y'  # Zwraca True, jeśli odpowiedź to 'y', w przeciwnym razie False
