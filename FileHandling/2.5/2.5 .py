# Tworzy listę zakupów na podstawie nazw produktów


# Nazwa pliku 
shopping_list = 'shopping_list.txt'

# Funkcja dodająca nazwę produktu 
def add_product(file_name, product_name):
    with open(file_name, 'a') as file:  # Otwiera plik w trybie dopisywania ('a')
        file.write(product_name + '\n')  # Zapisuje produkt i przechodzi do nowej linii


product = ""
while product != "0":  # Pętla dopóki nie wpisze '0'
    product = input('Wpisz nazwę produktu (0 kończy): ')  
    if product == '0':  
        print("Tworzenie listy zakupów zostało zakończone.")  
    else:
        add_product(shopping_list, product)  # Jeśli produkt jest inny niż '0', dodaje produkt do pliku
