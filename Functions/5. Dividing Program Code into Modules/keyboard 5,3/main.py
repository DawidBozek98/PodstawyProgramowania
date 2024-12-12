# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed

# Importujemy nasz własny moduł, który zawiera funkcje do wczytywania danych
import keyboard  # Importujemy funkcje z pliku keyboard.py

# Wczytujemy dane o pracowniku
first_name = keyboard.input_string('Enter name: ')  # Wczytanie imienia
last_name = keyboard.input_string('Enter last name: ')  # Wczytanie nazwiska
age = keyboard.input_integer('Enter age: ')  # Wczytanie wieku (liczba całkowita)
salary = keyboard.input_real('Enter salary: ')  # Wczytanie wynagrodzenia (liczba zmiennoprzecinkowa)
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')  # Wczytanie, czy ukryć wynagrodzenie (boolean)

# Drukowanie danych pracownika
print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)  # Imię i nazwisko
print('Age:', age)  # Wiek

# Warunkowe wyświetlanie wynagrodzenia
if is_salary_hidden:
    print('Salary: Hidden')  # Jeśli wynagrodzenie ma być ukryte
else:
    print('Salary:', salary)  # Jeśli wynagrodzenie ma być widoczne
