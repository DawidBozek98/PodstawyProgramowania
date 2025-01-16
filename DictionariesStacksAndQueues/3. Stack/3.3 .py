import queue

# Funkcja sprawdzająca poprawność nawiasów
def brackets_ok(expression):
    stack = queue.LifoQueue()  
    # Iteruje przez każdy znak
    for char in expression:
        if char in "({[":  # Sprawdza otwierające nawiasy
            stack.put(char)  # Dodaje na stos
        elif char in ")}]":  # Sprawdza zamykające nawiasy
            if stack.empty():
                return False  # Brak nawiasu otwierającego
            top = stack.get()  # Pobiera element z góry stosu
            # Sprawdza, czy nawias pasuje
            if char == ")" and top != "(":
                return False
            elif char == "}" and top != "{":
                return False
            elif char == "]" and top != "[":
                return False
    return stack.empty()  # Jeśli stos jest pusty, nawiasy są poprawne

# Wyrażenia do sprawdzenia
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # ok
expression2 = "[(2+3]/4)"                 # nie ok
expression3 = "(2-3*4+(5/6)"              # nie ok

# Sprawdza pierwsze wyrażenie
if brackets_ok(expression1):
    print("Expression 1: Brackets are OK")
else:
    print("Expression 1: Brackets are NOT correct")

# Sprawdza drugie wyrażenie
if brackets_ok(expression2):
    print("Expression 2: Brackets are OK")
else:
    print("Expression 2: Brackets are NOT correct")

# Sprawdza trzecie wyrażenie
if brackets_ok(expression3):
    print("Expression 3: Brackets are OK")
else:
    print("Expression 3: Brackets are NOT correct")
