# Funkcja zwracająca pełną nazwę dnia tygodnia na podstawie jego numeru

def day_name(day_number):

    # Początkowo wynik jest pusty
    result = ''

    # Sprawdzenie, jaki dzień odpowiada podanemu numerowi
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
    else:
        # Jeśli numer dnia jest poza zakresem 1-7, zwróć błąd
        result = 'Invalid day number'

   
    return result

# Nie było wymagane ale dla contentu lubię dać try catch :)
try:
    day_number = int(input('Enter a day number (1-7): '))
    
    print('The name of day', day_number, 'in the week is', day_name(day_number))
    
except ValueError:
    print('Invalid input. Please enter a valid number between 1 and 7.')
