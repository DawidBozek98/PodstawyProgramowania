# Funkcja sprawdzająca, czy co najmniej jedna z liczb jest ujemna

def f(n1, n2, n3):
    # Zwraca True, jeśli którakolwiek z liczb jest mniejsza od 0
    return n1 < 0 or n2 < 0 or n3 < 0
