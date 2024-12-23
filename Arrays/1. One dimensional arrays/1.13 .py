# Ceny 10 produktów w sklepie komputerowym
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Liczba jednostek dostępnych dla każdego produktu
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# Zmienna do sumowania łącznej wartości towarów
total_value = 0

# Pętla przeliczająca wartość każdego produktu
for price, quantity in zip(product_prices, product_quantities):
    total_value += price * quantity  # Mnożymy cenę przez ilość 


print("Total value of all products in the store:", round(total_value, 2))
