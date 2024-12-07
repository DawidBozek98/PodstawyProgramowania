

# Program wypisujący liczby od 1 do 30 z odpowiednimi słowami

for number in range(1, 31):  # Liczymy od 1 do 30
    if number % 3 == 0 and number % 5 == 0:
        print("BINGO", end=" ")  # jest podzielna przez 3 i 5
    elif number % 3 == 0:
        print("THREE", end=" ")  # jest podzielna przez 3
    elif number % 5 == 0:
        print("FIVE", end=" ")  # jest podzielna przez 5
    else:
        print(number, end=" ")  #  nie jest podzielna ani przez 3, ani przez 5
