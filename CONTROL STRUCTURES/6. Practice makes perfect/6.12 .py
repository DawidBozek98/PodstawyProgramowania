# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00

number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

# Sprawdzanie, czy liczba zakupionych produktów przekracza 2
if number_of_products > 2:
    # Obliczanie rabatu 
    discount_price = product_price * 0.75  # 25% rabatu
