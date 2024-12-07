###
# Calculates the number of days in a month
#
# Reads the month number from the user

month = int(input('Enter month number (1..12): ')) # Wczytywanie numeru miesiąca

# Sprawdzam liczbę dni w miesiącu
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31  # Miesiące z 31 dniami
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30  # Miesiące z 30 dniami
elif month == 2:
    days = 28  # Luty 28 dni



print(f'Month {month} has {days} days')