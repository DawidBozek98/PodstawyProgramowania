import vending_machine

#Testujemy kwoty do zapłaty
amounts = [23, 8, 2, 0]


for amount in amounts:
    print(f'Minimum coins for {amount} PLN: {vending_machine.f(amount)}')
