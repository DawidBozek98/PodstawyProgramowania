import queue

# Tworzy kolejkę plików do wydruku
files_to_print = queue.Queue()

while True:
    # Wyświetla menu
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')
    
    if menu == '1':
        # Dodaje plik do kolejki
        file_name = input('Enter file name to print: ')
        files_to_print.put(file_name)  # Dodaje plik na koniec kolejki
        
    elif menu == '2':
        # Sprawdza, czy kolejka nie jest pusta
        if not files_to_print.empty():
            file_to_print = files_to_print.get()  # Pobiera pierwszy plik z kolejki
            print(f'File {file_to_print} is currently being printed.')
        else:
            print('No files in the queue to print.')
    
    elif menu == '0':
        break
