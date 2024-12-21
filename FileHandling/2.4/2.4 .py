# Zapisuje do pliku listę pracowników zatrudnionych na określonym stanowisku

# Nazwy plików
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Stanowisko
job_title = 'Software Engineer'

# Otwórz plik z pracownikami i plik docelowy do zapisu
with open(employees_file, 'r') as employees:
    with open(position_file, 'w') as output_file:
        # Przechodzimy przez każdą linię w pliku
        for line in employees:
            # Sprawdzamy, czy w linii znajduje się poszukiwane stanowisko
            if job_title in line:
                # Zapisujemy linię do pliku, jeśli pracownik jest Software Engineer
                output_file.write(line)
