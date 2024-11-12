#5.4

amount = float(input('Podaj kwotę: '))# funkcja float bo liczba może być z przecinkiem
VAT = amount * 0.23

print(f'Kwota: {amount: .2f}') #.2f zaokrąglenie do 2 miejsc po przecinku
print(f'Vat 23%: {VAT:.2f}')
