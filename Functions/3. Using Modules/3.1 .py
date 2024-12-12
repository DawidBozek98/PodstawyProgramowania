###
# To use the functions available in an external module,
# you must include that module in your program.

import math

# Obliczanie pierwiastka kwadratowego z 7
square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

# Obliczanie logarytmu naturalnego z 5
natural_log = math.log(5)
print('The natural logarithm of 5 is', natural_log)

# math.sin() działa na radianach, więc konwertujemy 90 stopni na radiany
sine_90 = math.sin(math.radians(90))
print('The sine of 90 degrees is', sine_90)
