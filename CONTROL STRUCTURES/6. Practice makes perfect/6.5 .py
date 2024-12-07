###
# Program that simulates the operation of an electronic thermometer.
#

try:
    # Pobranie temperatury od użytkownika
    temperature = int(input("Enter degrees: "))  #Chciałem ułatwić test, przy okazji zobaczyłem jak wygląda try catch

    # Sprawdzanie temperatury i wyświetlanie odpowiedniego komunikatu
    if temperature > 35:
        print("It is extremely hot")
    elif temperature > 30:
        print("It is hot")
    elif temperature >= 15:
        print("It is warm")
    elif temperature >= 0:
        print("It is cold")
    else:
        print("Warning, frost")

except ValueError:  # w przypadku kiedy użytkownik nie poda liczby
    print("Invalid input! Please enter a valid number.")
