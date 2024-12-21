import csv

# Funkcja do przetwarzania pliku CSV
def process_csv(file_name):
    with open(file_name, mode='r') as file:
        # Otwieramy plik CSV
        reader = csv.DictReader(file)  # Korzystamy z DictReader, aby łatwo odwoływać się do nazw kolumn
        
        print("GRAPHIC DESIGNERS")
        print("=================")
        
        # Przechodzimy przez każdy wiersz w pliku
        for row in reader:
            # Sprawdzamy, czy stanowisko to 'Graphic Designer'
            if row['Job Title'] == 'Graphic Designer':
                # Wypisujemy imię, nazwisko i email
                print(f"{row['First Name']} {row['Last Name']},{row['Email']}")

# Główna część programu
process_csv('it_company.csv')
