import csv

# Funkcja, która wczytuje dane z pliku CSV
def read_books(file_name):
    books = []
    try:
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)  # Używamy DictReader, aby łatwiej odwoływać się do kolumn
            for row in reader:
                books.append(row)  # Dodajemy każdy wiersz (książkę) do listy
    except FileNotFoundError:
        print(f"Plik {file_name} nie istnieje!")
    return books

# Funkcja, która zapisuje książki do odpowiedniego pliku w zależności od gatunku
def save_books_by_genre(books, genre):
    # Wybieramy odpowiedni plik na podstawie gatunku
    if genre == 'Fantasy':
        file_name = 'books_fantasy.txt'
    elif genre == 'Historical':
        file_name = 'books_historical.txt'
    elif genre == 'Romance':
        file_name = 'books_romance.txt'
    elif genre == 'Classic':
        file_name = 'books_classic.txt'
    else:
        print(f"Nieobsługiwany gatunek: {genre}")
        return
    
    # Zapisujemy książki do odpowiedniego pliku
    with open(file_name, 'w') as file:
        for book in books:
            if book['Genre'] == genre:  # Sprawdzamy, czy książka należy do danego gatunku
                file.write(f"{book['Title']}, {book['Author']}, {book['Genre']}\n")
                print(f"Zapisano: {book['Title']} - {book['Author']}")

# Główna funkcja
def main():
    books = read_books('books.csv')  # Wczytujemy książki z pliku CSV

    # Zapytujemy użytkownika, do jakiego gatunku chcemy zapisać książki
    genre = input("Podaj gatunek (Fantasy, Historical, Romance, Classic): ").capitalize()

    # Zapisujemy książki do odpowiedniego pliku
    save_books_by_genre(books, genre)

main()
