###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number 1..12: '))
quater = 0 #ustalamy wartość początkową na 0 
if month >= 10:
    quater = 4
elif month >= 7:
    quater = 3
elif month >= 4:
    quater = 2
else:
    month  >= 1
    quater = 1

    

print(f'Month {month} is in quarter {quater}')