# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71


price = float(input('Podaj cenę produktu: '))
discount_percentage = float(input('Podaj procentową wartość rabatu: '))
reduction = price * (discount_percentage / 100)
price_with_discount = price - reduction

print(f'Cena przed rabatem {price:.2f}')
print(f'Procent rabatu {discount_percentage:.2f}')
print(f'Rabat {reduction:.2f}')
print(f'Cena po rabacie {price_with_discount:.2f}')