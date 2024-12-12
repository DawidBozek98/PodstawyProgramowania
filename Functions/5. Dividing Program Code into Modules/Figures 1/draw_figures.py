# Importujemy funkcję do rysowania kwadratu z pliku figures.py
import turtle
from figures import draw_square  # importujemy naszą funkcję

# Ustawienia ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")

# Długość boku kwadratu
side_length = 100

# Rysujemy kwadrat
draw_square(side_length)

# Zakończenie programu
window.mainloop()
