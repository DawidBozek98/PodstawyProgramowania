# Program do generowania kuponu lotto

# Iterujemy po liczbach od 1 do 7 (to będą nasze kolumny)
for i in range(1, 8):
    # W każdej kolumnie wypisujemy liczby od i do 49, z krokiem 7
    for j in range(i, 50, 7):
        print(j, end=" ")
    # Po wypisaniu liczb w jednej kolumnie przechodzimy do nowej linii
    print()
