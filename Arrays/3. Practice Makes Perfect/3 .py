import random  # Importujemy moduł random, żeby generować losowe liczby

# arr1: Prosta lista z określonymi wartościami
arr1 = [3, 7, 1, 0, 4]  # Lista zawiera liczby 3, 7, 1, 0, 4

# arr2: Tablica dwuwymiarowa z dwoma elementami w każdym wierszu

arr2 = [[2, 3], [7, 1], [0, 4]]  

# arr3: Lista z 5 elementami, z których każdy to 7
arr3 = [7 for i in range(5)]  

# arr4: Lista liczb od 1 do 9
arr4 = [i for i in range(1, 10)]  # Tworzymy listę liczb od 1 do 9

# arr5: Lista liczb parzystych od 2 do 18
arr5 = [i * 2 for i in range(1, 10)]  # Tworzymy listę liczb pomnożonych przez 2 (od 2 do 18)

# arr6: Lista 10 losowych liczb z przedziału 1-20
arr6 = [random.randint(1, 20) for i in range(10)]  # Losujemy 10 liczb z zakresu 1-20

# arr7: Lista 5 pustych list
arr7 = [[] for i in range(5)]  # Tworzymy 5 pustych list

# arr8: Tablica 4 wierszy, z których każdy zawiera dwie jedynki
arr8 = [[1 for i in range(2)] for j in range(4)]  # W każdym wierszu są dwie jedynki

# arr9: Tablica 5 wierszy, z których każdy zawiera 3 losowe liczby
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]  # Losujemy 3 liczby w każdym wierszu

# arr10: Tablica z wartościami 4, 0, 3
arr10 = [4, 0, 3]  # Lista zawiera liczby 4, 0, 3

# arr11: Tablica o 15 elementach wypełnionych zerami
arr11 = [0] * 15  # Lista zawiera 15 zer

# arr12: Tablica z 10 losowymi liczbami z zakresu 1-30
arr12 = [random.randint(1, 30) for i in range(10)]  # Losujemy 10 liczb z zakresu 1-30

# arr13: Tablica z 20 losowymi liczbami 0 lub 1
arr13 = [random.choice([0, 1]) for i in range(20)]


# arr14: Tablica 5 wierszy, z których każdy zawiera dwie wartości False
arr14 = [[False, False] for i in range(5)]  # Tworzymy 5 wierszy, w każdym są dwie wartości False

print("arr1:", arr1)  
print("arr2:", arr2)  
print("arr3:", arr3)  
print("arr4:", arr4)  
print("arr5:", arr5)  
print("arr6:", arr6)  
print("arr7:", arr7)  
print("arr8:", arr8)  
print("arr9:", arr9)  
print("arr10:", arr10)  
print("arr11:", arr11)  
print("arr12:", arr12)  
print("arr13:", arr13)  
print("arr14:", arr14)  
