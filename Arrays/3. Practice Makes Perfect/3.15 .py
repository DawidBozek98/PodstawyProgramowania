# Definiujemy krotkę
my_tuple = (10, 20, 30, 40, 50)

# Wypisujemy oryginalną krotkę
print("Tuple:", end=" ")
print(*my_tuple, sep=", ")

# Odwracamy krotkę i wypisujemy odwróconą kolejność
reversed_tuple = my_tuple[::-1]
print("Reverse order:", end=" ")
print(*reversed_tuple, sep=", ")
