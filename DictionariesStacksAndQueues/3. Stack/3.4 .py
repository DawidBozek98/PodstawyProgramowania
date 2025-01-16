import queue

def to_binary(number):
    stack = queue.LifoQueue()  # Tworzy stos

    # Dzielenie liczby przez 2 i dodawanie reszty do stosu
    while number > 0:
        remainder = number % 2  # Reszta z dzielenia przez 2
        stack.put(remainder)  # Dodaje resztę do stosu
        number = number // 2  # (całkowite dzielenie)
    
    # Tworzy wynik binarny przez pobieranie elementów ze stosu
    binary_number = ""
    while not stack.empty():
        binary_number += str(stack.get())  # Pobiera i dodaje element z stosu
    
    return binary_number


number = int(input("Enter a natural number: "))

binary_number = to_binary(number)

print(f"Natural number: {number}")
print(f"Binary number: {binary_number}")
