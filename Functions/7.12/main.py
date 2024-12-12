import asterisk_pattern

# Przykładowe wartości 
test_values = [4, 1, 0, 7]

# Testowanie funkcji 

for n in test_values:
    
    result = asterisk_pattern.f(n)
    print(f"f({n}) returns: '{result}'")
