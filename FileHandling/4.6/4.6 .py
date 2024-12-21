def count_file_details(filename):
    try:
        
        line_count = 0
        word_count = 0
        char_count = 0

        file = open(filename, 'r')

        # Przechodzimy przez każdą linię w pliku
        for line in file:
            line_count += 1  # Liczymy linie
            word_count += len(line.split())  # Liczymy słowa (split dzieli tekst na słowa)
            char_count += len(line)  # Liczymy znaki łącznie ze spacjami

        file.close()

        print("File name:", filename)
        print("Number of lines:", line_count)
        print("Number of characters:", char_count)
        print("Number of words:", word_count)

    except:
        print("Error: The file does not exist.")

# Główna część programu
filename = input("Enter the name of the file: ")  # Pobieramy nazwę pliku od użytkownika
count_file_details(filename)  # Wywołujemy funkcję z nazwą pliku
