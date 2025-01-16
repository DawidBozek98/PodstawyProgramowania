import csv

# Krok 1: Wczytaj dane o województwach z pliku CSV
provinces = {}
with open('province.csv', mode='r', encoding='utf-8') as file: # miałem problem z rozkodowanie csv, dodałem encoding utf-8
    reader = csv.reader(file)
    next(reader)  # Pomijamy nagłówek
    for row in reader:
        letter, province_name = row
        provinces[letter] = province_name  # Zapisz dane do słownika

# Inicjalizacja słownika do liczenia pojazdów
vehicle_count = {province: 0 for province in provinces.values()}

# Krok 2: Wczytaj dane o pojazdach z pliku vehicle.txt
with open('vehicle.txt', mode='r') as file:
    for line in file:
        registration_number = line.strip()  # Usuwanie zbędnych spacji
        first_letter = registration_number[0]  # Pierwsza litera rejestracji
        if first_letter in provinces:
            province_name = provinces[first_letter]
            vehicle_count[province_name] += 1  # Zwiększ liczbę pojazdów

# Krok 3: Wyświetl wyniki
print("Liczba pojazdów w poszczególnych województwach:")
for province, count in vehicle_count.items():
    print(f"{province}: {count} pojazdów")
