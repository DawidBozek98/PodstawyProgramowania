import check_negative

# Przykładowe dane wejściowe
numbers = [(11, 6, -4), (5, 4, 14), (-1, 0, 0), (3, -2, 1)]

# Testowanie funkcji 
for n1, n2, n3 in numbers:

    
    result = check_negative.f(n1, n2, n3)
    print(f"For numbers {n1}, {n2}, {n3}, at least one is negative: {result}")
