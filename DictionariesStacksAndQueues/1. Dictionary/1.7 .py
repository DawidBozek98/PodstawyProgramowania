store_inventory = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

print("Product list and quantities:")
for product, quantity in store_inventory.items():
    print(f"{product}: {quantity}")

# Obliczanie łącznej liczby produktów
total_products = sum(store_inventory.values())
print(f"\nTotal number of products: {total_products}")
