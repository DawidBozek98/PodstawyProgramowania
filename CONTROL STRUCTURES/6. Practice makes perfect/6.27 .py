# for i in range(6, -1, -3):   Iteruje od 6 do 0 (z krokiem -3)
#     for j in range(1, 4):   Iteruje od 1 do 3 (czyli 1, 2, 3)
#         print(f'{i+j}', end=' ')  Drukuje wynik (i + j), bez przejścia do nowej linii
#     print()  #Nowa linia po każdym zakończeniu wewnętrznej pętli


i = 6  # Zaczynamy od 6
while i >= 0:  # Warunek dla zewnętrznej pętli
    j = 1 
    while j <= 3:  # Warunek dla wewnętrznej pętli
        print(f'{i + j}', end=' ')  
        j += 1  # Zwiększamy j o 1
    print()  # Nowa linia po zakończeniu wewnętrznej pętli
    i -= 3  # Zmniejszamy i o 3
