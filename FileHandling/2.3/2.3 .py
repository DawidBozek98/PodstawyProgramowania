# Tworzy kopię pliku tekstowego

# Nazwy plików
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# Odczyt zawartości pliku oryginalnego
with open(original_file, 'r') as source_file:
    content = source_file.read()  # Odczyt całej zawartości pliku

# Zapis zawartości do nowego pliku (kopii)
with open(target_file, 'w') as destination_file:
    destination_file.write(content)  # Zapis danych do pliku docelowego
