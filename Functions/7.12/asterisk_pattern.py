# Funkcja generująca ciąg gwiazdek oddzielonych znakiem ukośnika

def f(n):
    
    # Zwraca ciąg n gwiazdek rozdzielonych ukośnikiem
    return "*/" * (n - 1) + "*" if n > 0 else ""
