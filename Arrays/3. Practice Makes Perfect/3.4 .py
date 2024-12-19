# Tablica zawierająca liczby
numbers = [-15, 8, -31, 47, -2, 19]

# Zakładamy, że pierwszy element tablicy jest zarówno maksymalny, jak i minimalny
max_num = numbers[0]
min_num = numbers[0]

# Przechodzimy przez tablicę i porównujemy każdy element z aktualnym maksymalnym i minimalnym
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num


print("Maximum number:", max_num)
print("Minimum number:", min_num)
