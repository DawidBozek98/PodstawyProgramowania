# 5x5 seating arrangement
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

# Funkcja zwracająca łączną liczbę miejsc w kinie
def seats_total(seats):
   total = 0
   for row in seats:
       total += len(row)  # Zliczamy liczbę miejsc w każdym wierszu
   return total

# Funkcja zwracająca liczbę dostępnych miejsc (A)
def seats_available(seats):
   available = 0
   for row in seats:
       available += row.count('A')  # Liczymy wystąpienia 'A' w każdym wierszu
   return available

# Funkcja zwracająca liczbę zarezerwowanych miejsc (B)
def seats_booked(seats):
   booked = 0
   for row in seats:
       booked += row.count('B')  # Liczymy wystąpienia 'B' w każdym wierszu
   return booked

# Funkcja zwracająca status miejsca w kinie
def seat_status(seats, row, place):
   # Zwracamy status miejsca w danym wierszu i kolumnie
   return 'Available' if seats[row][place] == 'A' else 'Booked'

# Wypisanie informacji
print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 0, 0))  # Rząd 1, miejsce 1 (indeks 0)
print('Seat in row 5, place 5:', seat_status(cinema_seats, 4, 4))  # Rząd 5, miejsce 5 (indeks 4)
print('Seat in row 3, place 5:', seat_status(cinema_seats, 2, 4))  # Rząd 3, miejsce 5 (indeks 4)
