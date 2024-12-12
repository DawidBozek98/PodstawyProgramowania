# Funkcja, która zwraca nazwę miesiąca na podstawie numeru miesiąca (1-12)
def month(n):
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ] # Tworzymy tablicę z nazwami miesięcy
    if 1 <= n <= 12:
        return months[n - 1]  # Zwraca nazwę miesiąca musi być -1, przy samym n nie działa
    else:
        return "Invalid month number"  # Obsługuje błędne numery miesięcy
