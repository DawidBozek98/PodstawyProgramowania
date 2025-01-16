import queue

# odwracanie tekstu za pomocą stosu
def reverse_string(input_string):
   
    stack = queue.LifoQueue()

    # Dodajemy każdą literę do stosu
    for char in input_string:
        stack.put(char)

    # Zdejmujemy litery ze stosu, aby utworzyć odwrócony tekst
    reversed_string = ''
    while not stack.empty():
        reversed_string += stack.get()

    return reversed_string


text = input("Enter the text to reverse: ")

# Wywołujemy odwrócenie 
reversed_text = reverse_string(text)


print("Reversed text:", reversed_text)
