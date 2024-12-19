# 3x3 plansza do gry w Tic-Tac-Toe
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

# Przechodzimy przez każdy wiersz planszy
for row in tic_tac_toe_board:
    # Wypisujemy każdy element w wierszu, oddzielając je spacją
    for element in row:
        print(element, end=" ")
    # Po wypisaniu całego wiersza przechodzimy do nowej linii
    print()
