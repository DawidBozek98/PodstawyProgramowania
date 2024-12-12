# Funkcja rysująca kwadrat o zadanej długości boku
import turtle

def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

# Funkcja rysująca trójkąt równoramienny
def draw_triangle(length):
    for i in range(2):
        turtle.forward(length)
        turtle.left(120)
    turtle.forward(length)

# Funkcja rysująca prostokąt o zadanych bokach
def draw_rectangle(length_a, length_b):
    for i in range(2):
        turtle.forward(length_a)
        turtle.left(90)
        turtle.forward(length_b)
        turtle.left(90)
