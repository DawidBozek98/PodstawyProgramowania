# Funkcja do obliczenia i zapisania potęg liczb od 1 do 100
def calculate_powers():
    with open("powers.txt", "w") as file:  # Otwieramy plik do zapisu
        for i in range(1, 101):
            second_power = i ** 2  # Druga potęga
            third_power = i ** 3   # Trzecia potęga
            file.write(f"{i},{second_power},{third_power}\n")  # Zapisujemy wynik do pliku
            print(f"{i},{second_power},{third_power}")  # Wypisujemy wynik na ekranie

# Wywołanie funkcji
calculate_powers()
