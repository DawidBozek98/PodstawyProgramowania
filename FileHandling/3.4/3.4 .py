import re  # moduł do pracy z wyrażeniami regularnymi

# nazwa pliku 
email_file = 'report.txt'

# otwieramy plik 
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# wyrażenie regularne do dopasowania kwot 
pattern = r'€?\s?\d+(?:,\d{1,2})?'  # dopasowuje kwoty z symbolem Euro

# wyciągamy wszystkie kwoty z tekstu
amounts = re.findall(pattern, email)

# obliczamy całkowitą wydaną kwotę
total_spent = 0
for amount in amounts:
    # usuwamy symbol Euro i spacje, zamieniamy przecinki na kropki 
    amount = amount.replace('€', '').replace(' ', '').replace(',', '.')
    total_spent += float(amount)  # konwertujemy do float i dodajemy do sumy

print(f'Całkowita wydana kwota: €{total_spent:.2f}')
