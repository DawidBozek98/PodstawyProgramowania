# Symulator bankomatu (ATM)
# Użytkownik może sprawdzić saldo, wpłacić środki, wypłacić środki, sprawdzić PIN i zmienić PIN.

balance = 1000  # Początkowy stan konta
pin = '1111'  # Początkowy PIN, 4-cyfrowy

def check_pin(current_pin):
    """Sprawdza poprawność PIN-u."""
    # Użytkownik wpisuje PIN. Funkcja zwraca True, jeśli PIN jest poprawny, inaczej False.
    return input("Enter your PIN: ") == current_pin

def change_pin():
    """Zmienia PIN, jeśli nowy PIN spełnia warunki."""
    # Użytkownik wprowadza nowy PIN, który musi mieć 4 cyfry i być poprawnie potwierdzony.
    new_pin = input("Enter a new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit() and new_pin == input("Confirm your new PIN: "):
        print("PIN successfully changed.")
        return new_pin  # Zwraca nowy PIN, jeśli zmiana się powiodła
    print("PIN change failed. Try again.")
    return pin  # Zwraca stary PIN, jeśli zmiana się nie powiodła

while True:
    # Wyświetlenie menu opcji bankomatu
    print("\nATM Menu:")
    print("1. Check balance")  # Opcja: sprawdzenie salda
    print("2. Deposit")       # Opcja: wpłata środków
    print("3. Withdraw")      # Opcja: wypłata środków
    print("4. Change PIN")    # Opcja: zmiana PIN-u
    print("5. Exit")          # Opcja: wyjście z programu

    choice = input("Choose an option (1-5): ")  # Pobranie wyboru użytkownika

    if choice == '1':  # Opcja 1: Sprawdzenie salda
        if check_pin(pin):  # Sprawdzamy, czy PIN jest poprawny
            print(f"Your current balance is: €{balance}")
        else:
            print("Incorrect PIN.")  # Błędny PIN
    elif choice == '2':  # Opcja 2: Wpłata środków
        if check_pin(pin):  # Sprawdzamy, czy PIN jest poprawny
            balance += float(input("Enter the amount to deposit: "))  # Dodajemy wpłaconą kwotę do salda
            print(f"New balance: €{balance}")  # Wyświetlenie nowego salda
        else:
            print("Incorrect PIN.")  # Błędny PIN
    elif choice == '3':  # Opcja 3: Wypłata środków
        if check_pin(pin):  # Sprawdzamy, czy PIN jest poprawny
            amount = float(input("Enter the amount to withdraw: "))  # Pobieramy kwotę do wypłaty
            if amount <= balance:  # Sprawdzamy, czy saldo jest wystarczające
                balance -= amount  # Odejmujemy kwotę od salda
                print(f"New balance: €{balance}")  # Wyświetlenie nowego salda
            else:
                print("Insufficient balance.")  # Komunikat o niewystarczającym saldzie
        else:
            print("Incorrect PIN.")  # Błędny PIN
    elif choice == '4':  # Opcja 4: Zmiana PIN-u
        if check_pin(pin):  # Sprawdzamy, czy PIN jest poprawny
            pin = change_pin()  # Zmieniamy PIN
        else:
            print("Incorrect PIN.")  # Błędny PIN
    elif choice == '5':  # Opcja 5: Wyjście z programu
        print("Exiting... Thank you for using the ATM!")  # Komunikat o zakończeniu
        break  # Kończymy pętlę
    else:
        print("Invalid option. Please try again.")  # Komunikat o niepoprawnym wyborze

#nie zrobiłem tego samodzielnie trochę zbyt skomplikowane na start