import re  # Importowanie modułu 're' 

username = input("Wprowadź nazwę użytkownika: ")
password = input("Wprowadź hasło: ")

# Wzorzec 
# co najmniej 6 znaków
# tylko małe litery
username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^[A-Za-z0-9_]{8,}$'

# Sprawdzanie, czy nazwa użytkownika i hasło pasują do wzorców
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)


if username_match and password_match:
    print("Nazwa użytkownika i hasło są poprawne.")
else:
    if not username_match:
        print("Nazwa użytkownika jest niepoprawna. Musi mieć co najmniej 6 znaków i zawierać tylko małe litery.")
    if not password_match:
        print("Hasło jest niepoprawne. Musi mieć co najmniej 8 znaków i zawierać tylko litery, cyfry oraz znak podkreślenia.")
