# Tworzę dwuwymiarową tablicę 3x5 z liczbami całkowitymi
arr = [
    [1, 2, 3, 4, 5],  
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15] 
]

# Wypisuję zawartość tablicy przed zmianą
print("Tablica przed zmianą:")
for row in arr:
    print(row)  

# Zamieniam pierwszy i ostatni element w każdej kolumnie
for row in arr:
    row[0], row[4] = row[4], row[0]  # Zamiana elementów w pierwszej i ostatniej kolumnie


print("\nTablica po zamianie pierwszej i ostatniej kolumny:")
for row in arr:
    print(row)  
