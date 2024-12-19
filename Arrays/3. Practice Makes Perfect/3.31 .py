
arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]] # Dwuwymiarowa tablica


min_value = arr[0][0]
max_value = arr[0][0]

# pozycje najmniejszej i największej liczby
min_pos = (0, 0)
max_pos = (0, 0)



for i in range(len(arr)):          # Pętla po wierszach
    for j in range(len(arr[i])):  # Pętla po kolumnach w danym wierszu
        # Sprawdzam, czy napotkana liczba jest mniejsza niż dotychczasowa najmniejsza
        if arr[i][j] < min_value:
            # Jeśli tak, to aktualizuję zmienną min_value 
            min_value = arr[i][j]
            min_pos = (i, j)
        
        # Sprawdzam, czy napotkana liczba jest większa niż dotychczasowa największa
        if arr[i][j] > max_value:
            # jeśli tak aktualizuję zmienną max_value 
            max_value = arr[i][j]
            max_pos = (i, j)


print("Najmniejsza liczba:", min_value, "znajduje się w wierszu", min_pos[0], "i kolumnie", min_pos[1])


print("Największa liczba:", max_value, "znajduje się w wierszu", max_pos[0], "i kolumnie", max_pos[1])
