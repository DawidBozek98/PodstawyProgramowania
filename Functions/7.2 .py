# Funkcja dodająca dwie liczby
def add(a, b):
    return a + b

# Funkcja odejmująca dwie liczby
def subtract(a, b):
    return a - b

# Funkcja główna, w której testujemy nasze funkcje
def main():
    # Ta część kodu wykona się tylko, gdy skrypt jest uruchamiany bezpośrednio
    x = 10
    y = 5
    print(f"Add: {add(x, y)}")  
    print(f"Subtract: {subtract(x, y)}")  

# Upewniamy się, że funkcja main() uruchomi się tylko wtedy, gdy skrypt jest uruchamiany bezpośrednio
if __name__ == "__main__":
    main()  # Wywołujemy funkcję main


#Nie mogę się przyzwyczaić do tych klas main tutaj, poczytać o tym