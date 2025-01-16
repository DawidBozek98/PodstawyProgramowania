import queue

# Tworzymy kolejkę
customers_queue = queue.Queue()

# Zmienna do generowania numeru ticketu
ticket_number = 1

# Funkcja obsługująca nowych klientów
def add_customer():
    global ticket_number
    customers_queue.put(ticket_number)  # Dodajemy klienta do kolejki
    print(f"Klient z ticketem {ticket_number} czeka w kolejce.")
    ticket_number += 1  # Zwiększamy numer ticketu

# Funkcja do obsługi klienta
def serve_customer():
    if not customers_queue.empty():  # Sprawdzamy, czy są klienci
        served_customer = customers_queue.get()  # Usuwamy klienta z kolejki
        print(f"Obsługujemy klienta z ticketem {served_customer}.")
    else:
        print("Brak klientów w kolejce.")  # Jeśli kolejka jest pusta

# Przykład 
add_customer()  
add_customer()  
add_customer()  

serve_customer()  
serve_customer()  
serve_customer()  
serve_customer()  
