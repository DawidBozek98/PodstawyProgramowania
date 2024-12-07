




current_price = float(input("Enter current product price: "))
previous_price = float(input("Enter previous product price: "))


price_change_percentage = ((previous_price - current_price) / previous_price) * 100 # Obliczanie procentowej zmiany ceny

# Sprawdzenie, czy cena spadła o co najmniej 10%
if price_change_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(price_change_percentage)}%")
else:
    print("Price decrease is not sufficient for a recommendation.")
