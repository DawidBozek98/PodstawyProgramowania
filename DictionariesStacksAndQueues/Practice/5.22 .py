import json

# Tworzymy pusty słownik na dane produktu
product = {}

# Pobieranie danych o produkcie z klawiatury
product["name"] = input("Enter the product name: ").strip()  #  (string)
product["price"] = float(input("Enter the product price (e.g., 12.99): "))  # (float)
paid_input = input("Is the product paid? (yes/no): ").strip().lower()  # (bool)
product["paid"] = True if paid_input == "yes" else False  # Zamiana "yes/no" na True/False

# Zapis danych do pliku JSON
file_name = "product.json"
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print(f"Product data has been saved to {file_name}.")


# Enter the product name: Coffee Mug
# Enter the product price (e.g., 12.99): 14.50
# Is the product paid? (yes/no): yes