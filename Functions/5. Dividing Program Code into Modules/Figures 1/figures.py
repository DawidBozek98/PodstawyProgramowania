# Funkcja rysująca kwadrat o zadanej długości boku
import turtle

def draw_square(length):
    # Tworzymy obiekt turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Rysowanie kwadratu
    for i in range(4):
        pen.forward(length)
        pen.right(90)

    # Ukrywamy żółwia po narysowaniu
    pen.hideturtle()
