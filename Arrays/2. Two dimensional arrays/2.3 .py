# Miesięczne wydatki podzielone na tygodnie i kategorie
monthly_expenses = [
   [200, 50, 100],  # Tydzień 1 (żywność, transport, media)
   [180, 60, 110],  # Tydzień 2
   [220, 55, 105],  
   [210, 65, 95]    
]

# Inicjalizacja zmiennych do obliczenia sum dla każdej kategorii
food_expenses = 0
transport_expenses = 0
utilities_expenses = 0

# Inicjalizacja zmiennych do obliczenia sum dla każdego tygodnia
week_expenses = [0, 0, 0, 0]

# Obliczamy wydatki dla każdej kategorii i tygodnia
for week in range(4):  # Dla każdego tygodnia
    food_expenses += monthly_expenses[week][0]
    transport_expenses += monthly_expenses[week][1]
    utilities_expenses += monthly_expenses[week][2]
    
    # Obliczanie sumy wydatków w danym tygodniu
    week_expenses[week] = sum(monthly_expenses[week])

# Obliczamy całkowite wydatki w miesiącu
total_expenses = food_expenses + transport_expenses + utilities_expenses

# Wyświetlamy wyniki
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_expenses)
print('Transport:', transport_expenses)
print('Utilities:', utilities_expenses)
print('Week 1:', week_expenses[0])
print('Week 2:', week_expenses[1])
print('Week 3:', week_expenses[2])
print('Week 4:', week_expenses[3])
print('---------------')
print('TOTAL:', total_expenses)
