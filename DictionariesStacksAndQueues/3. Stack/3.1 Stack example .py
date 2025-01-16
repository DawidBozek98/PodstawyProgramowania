import queue

# Tworzy stos
stack = queue.LifoQueue()

# Dodaje liczby na stos
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Sumuje dwie ostatnie liczby
last_number = stack.get()  
second_last_number = stack.get()  
sum_last_two = last_number + second_last_number  # Suma dwóch ostatnich
print(f"Sum of the last two numbers: {sum_last_two}")

# Zwraca przedostatnią na stos
stack.put(second_last_number)

# Sumuje pozostałe elementy stosu
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()  

print(f"Sum of the remaining stack elements: {remaining_sum}")
