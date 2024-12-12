# Importujemy moduł month
import month

# Pobieramy numer miesiąca od użytkownika
month_number = int(input("Enter month number: "))

# Wywołujemy funkcję month() i wyświetlamy nazwę miesiąca
print(f"The name of month {month_number} is {month.month(month_number)}")
