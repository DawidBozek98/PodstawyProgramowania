# Program analizuje temperatury w marcu na podstawie wyników pomiarów

march_temperatures = [
   5, 8, 7, 6, 4, 3, 2, 1, -2, 0, 3, 4, 6, 7, 8, 9, 10, 12, 13, 15, 14, 16, 17, 19, 20, 21, 23, 24, 26, 28, 30
]

# Liczba pomiarów (dni)
num_measurements = len(march_temperatures)

# Średnia temperatura w miesiącu
average_temperature = sum(march_temperatures) / num_measurements

# Minimalna temperatura
min_temperature = min(march_temperatures)

# Maksymalna temperatura
max_temperature = max(march_temperatures)

# Liczba dni z temperaturą ujemną
negative_days = sum(1 for temp in march_temperatures if temp < 0)


print('TEMPERATURE REPORT')
print('====================')
print('Month: March')
print('Number of measurements:', num_measurements)
print('Average temperature in the month:', f"{average_temperature:.2f}°C")
print('Minimum temperature:', f"{min_temperature}°C")
print('Maximum temperature:', f"{max_temperature}°C")
print('Number of days with negative temperature:', negative_days)
