import binary_validator

# Przykładowe ciągi do sprawdzenia
binary_1 = "101101"
binary_2 = "1311a10100"

# Sprawdzamy, czy ciągi są poprawnymi numerami binarnymi
result_1 = binary_validator.f(binary_1)
result_2 = binary_validator.f(binary_2)

print(f'Is "{binary_1}" a valid binary number? {result_1}')
print(f'Is "{binary_2}" a valid binary number? {result_2}')
