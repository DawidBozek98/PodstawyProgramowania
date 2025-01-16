import json

# Funkcja do liczenia liczby pokoi
def count_rooms(data):
    # Licz unikalne numery pokoi
    room_numbers = {reservation["room_number"] for reservation in data["reservations"]}
    return len(room_numbers)

# Funkcja do liczenia rezerwacji
def count_reservations(data, paid_status):
    # Licz rezerwacje według statusu płatności
    return sum(1 for reservation in data["reservations"] if reservation["paid"] == paid_status)

# Funkcja do obliczania wartości rezerwacji
def calculate_total_value(data, paid_status):
    # Oblicz wartość rezerwacji
    return sum(reservation["nights"] * reservation["price_per_night"]
               for reservation in data["reservations"] if reservation["paid"] == paid_status)

# Funkcja główna
def print_summary(file_path):
    # Otwórz plik JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Wypisz liczbę pokoi
    num_rooms = count_rooms(data)
    print("Number of rooms:", num_rooms)

    # Wypisz liczbę rezerwacji opłaconych i nieopłaconych
    num_paid = count_reservations(data, paid_status=True)
    num_unpaid = count_reservations(data, paid_status=False)
    print("Number of paid reservations:", num_paid)
    print("Number of unpaid reservations:", num_unpaid)

    # Wypisz wartości rezerwacji
    total_paid_value = calculate_total_value(data, paid_status=True)
    total_unpaid_value = calculate_total_value(data, paid_status=False)
    print("Total value of paid reservations:", total_paid_value)
    print("Total value of unpaid reservations:", total_unpaid_value)


print_summary('reservations.json')
