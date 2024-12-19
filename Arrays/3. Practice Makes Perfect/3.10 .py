# Definicja dwóch tablic
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

# Wypisanie liczb z array1, które nie występują w array2
for num in array1:
    if num not in array2:
        print(num)
