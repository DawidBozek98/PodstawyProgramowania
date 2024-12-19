# Tworzę dwuwymiarową tablicę 3x5
arr = [
    [1, 2, 3, 4, 5],   # Pierwszy wiersz
    [6, 7, 8, 9, 10],  # Drugi wiersz
    [11, 12, 13, 14, 15]  # Trzeci wiersz
]

# Wypisuję zawartość tablicy przed zmianami
print("Tablica przed zmianą:")
for row in arr:
    print(row)  # Wypisuje każdy wiersz z tablicy

# Zamieniam pierwszy i ostatni wiersz
arr[0], arr[2] = arr[2], arr[0]

print("\nTablica po zamianie pierwszego i ostatniego wiersza:")
for row in arr:
    print(row)  
