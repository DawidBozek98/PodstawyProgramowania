# Importujemy funkcje do rysowania kształtów z pliku figures.py
import turtle
from figures import draw_square, draw_triangle, draw_rectangle

# Ustawienia ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tworzymy żółwia
pen = turtle.Turtle()
pen.speed(5)   

# Funkcja rysująca kształty w różnych lokalizacjach
def draw_figures():
    # Rysowanie kwadratu
    pen.penup()  # Podnosimy pióro, aby nie rysować podczas przemieszczania
    pen.goto(-200, 100)  # Przesuwamy żółwia do nowej lokalizacji
    pen.pendown()  # Kładziemy pióro, aby zacząć rysowanie
    draw_square(100)

    pen.penup()  # Podnosimy pióro, aby nie rysować podczas przemieszczania
    pen.goto(100, 100)  # Nowa lokalizacja
    pen.pendown()  # Kładziemy pióro, aby zacząć rysowanie
    draw_square(100)

    # Rysowanie trójkąta
    pen.penup()  # Podnosimy pióro, aby nie rysować podczas przemieszczania
    pen.goto(-200, -100)  # Nowa lokalizacja
    pen.pendown()  # Kładziemy pióro, aby zacząć rysowanie
    draw_triangle(100)

    pen.penup()  # Podnosimy pióro, aby nie rysować podczas przemieszczania
    pen.goto(100, -100)  # Nowa lokalizacja
    pen.pendown()  # Kładziemy pióro, aby zacząć rysowanie
    draw_triangle(100)

    # Rysowanie prostokąta
    pen.penup()  # Podnosimy pióro, aby nie rysować podczas przemieszczania
    pen.goto(-200, -300)  # Nowa lokalizacja
    pen.pendown()  # Kładziemy pióro, aby zacząć rysowanie
    draw_rectangle(150, 80)

    pen.penup()  # Podnosimy pióro, aby nie rysować podczas przemieszczania
    pen.goto(100, -300)  # Nowa lokalizacja
    pen.pendown()  # Kładziemy pióro, aby zacząć rysowanie
    draw_rectangle(150, 80)

# Rysujemy kształty
draw_figures()

# Ukrywamy żółwia i kończymy
pen.hideturtle()
window.mainloop()
