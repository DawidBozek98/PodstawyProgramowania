# Enter the amount in PLN: 18
# The amount of PLN 18 in coins:
# 5 PLN coins: 3
# 2 PLN coins: 1
# 1 PLN coins: 1



# Program do rozbijania kwoty na jak najmniejszą liczbę monet


amount = int(input("Enter the amount in PLN: "))

# Liczba monet 5 PLN
coins_5 = amount // 5  
amount = amount % 5  # reszta po podzieleniu przez 5

# Liczba monet 2 PLN
coins_2 = amount // 2  
amount = amount % 2  # reszta po podzieleniu przez 2

# Liczba monet 1 PLN
coins_1 = amount  # Pozostała kwota to liczba monet 1 PLN

# Wyświetlamy wynik
print(f"The amount of PLN in coins:")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")
