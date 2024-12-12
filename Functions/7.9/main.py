# Importujemy funkcję f z modułu digits_sum
import digits_sum

# Testujemy funkcję dla różnych przykładów
examples = [
    (3124, True),
    (3124, False),
    (20576, False),
    (20576, True),
    (13115, True)
]


for number, even in examples:
    result = digits_sum.f(number, even)
    print(f'f({number}, {even}) returns {result}')
