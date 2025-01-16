price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# Wyświetlanie przed rabatem
print("Prices before discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

#  wartość przed rabatem
total_before_discount = sum(price_list.values())
print(f"\nTotal value before discount: ${total_before_discount:.2f}")

# Zastosowanie rabatu 10% i zaokrąglanie cen
for product in price_list:
    price_list[product] = round(price_list[product] * 0.90, 2)

print("\nPrices after 10% discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")


total_after_discount = sum(price_list.values())
print(f"\nTotal value after discount: ${total_after_discount:.2f}")
