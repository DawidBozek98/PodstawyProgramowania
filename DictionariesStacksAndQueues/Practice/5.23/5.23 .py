import json  


with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)  # Załaduj dane JSON

# Wyświetl nagłówek tabeli
print(f"{'Date':<15}{'Buying Rate':<15}{'Selling Rate':<15}")
print("=" * 45)  # Linia podziału

# Iteruj po kursach wymiany
for rate in data['rates']:
    date = rate['effectiveDate']  
    bid = rate['bid']  
    ask = rate['ask']  
    #
    print(f"{date:<15}{bid:<15.4f}{ask:<15.4f}")
