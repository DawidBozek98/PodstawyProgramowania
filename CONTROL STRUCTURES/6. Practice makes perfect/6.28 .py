
# Program do wypisania pierwszych 20 liczb ciągu Fibonacciego

# Pierwsze dwie liczby Fibonacciego
a, b = 0, 1 # internet pomógł, normalnie pisałbym te dwie zmienne pod sobą 

# Licznik, który śledzi ilość wypisanych liczb
count = 0

# Pętla, która generuje i wypisuje liczby Fibonacciego
while count < 20:
    print(a, end=" ")  
    # Zaktualizuj wartości a i b, aby uzyskać kolejne liczby Fibonacciego
    a, b = b, a + b
    count += 1  # Zwiększ licznik
