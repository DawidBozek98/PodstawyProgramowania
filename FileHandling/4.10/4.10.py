import csv

# Funkcja do przetwarzania pliku CSV
def process_clothing_csv(file_name):
    with open(file_name, mode='r') as file:
        # Otwieramy plik CSV
        reader = csv.DictReader(file)  # Korzystamy z DictReader, aby łatwo odwoływać się do nazw kolumn
        
        # Sprawdzamy nagłówki, aby upewnić się, że są poprawne
        print("Column names:", reader.fieldnames)
        
        print("PRODUCTS UNDER 60 AND LESS THAN 40 IN STOCK")
        print("===========================================")
        
        # Przechodzimy przez każdy wiersz w pliku
        for row in reader:
            # Usuwamy ewentualne spacje z nazw kolumn
            row = {key.strip(): value for key, value in row.items()}
            
            # Sprawdzamy, czy cena jest mniejsza niż 60 i stan magazynowy mniejszy niż 40
            try:
                price = float(row['Price'])  # Zamieniamy cenę na liczbę zmiennoprzecinkową
                stock = int(row['Stock'])  # Zamieniamy stan magazynowy na liczbę całkowitą
                # Jeśli spełnia oba warunki, wypisujemy produkt
                if price < 60 and stock < 40:
                    print(f"{row['Product']}, ${price}, Stock: {stock}")
            except KeyError:
                # Jeśli nie ma odpowiednich danych, pomijamy ten wiersz
                continue
            except ValueError:
                # Jeśli napotkamy błąd konwersji, pomijamy ten wiersz
                continue

# Główna część programu
process_clothing_csv('clothing.csv')
