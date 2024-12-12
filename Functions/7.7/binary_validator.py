# Funkcja sprawdzająca, czy dany ciąg jest poprawnym numerem binarnym

def f(binary_number):
    
    # Sprawdzamy, czy ciąg zawiera tylko znaki '0' i '1'
    return all(char in '01' for char in binary_number)
