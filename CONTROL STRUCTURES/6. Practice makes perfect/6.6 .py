# The parking meter calculates the parking fee based on the number of hours the car 
# was parked according to the following rules:

# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
# Write a program that asks for the number of hours of parking, then calculates 
# and prints the correct fee.



hours = int(input("Enter the number of hours parked: ")) # Pobieramy liczbę godzin parkowania od użytkownika
# Sprawdzamy, która strefa opłaty dotyczy tej liczby godzin
if 1 <= hours <= 2:
    fee = 5  
elif 3 <= hours <= 6:
    fee = 15  
elif hours > 6:
    fee = 20  
else:
    fee = 0  # Jeżeli liczba godzin jest mniejsza niż 1, brak opłaty

print(f"The parking fee is {fee} PLN.")
