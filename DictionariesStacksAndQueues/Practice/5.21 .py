import json

# Słownik opisujący ulubioną książkę lub film
favourite = {
    "title": "The Lord of the Rings: The Fellowship of the Ring",
    "author_or_director": "J.R.R. Tolkien",
    "genre": "Fantasy",
    "year_of_release": 1954,  # Rok wydania
    "summary": "An epic tale of friendship, courage, and the journey to destroy a powerful ring."
}

# Nazwa pliku, do którego zapiszemy dane
file_name = "favourite.json"

# Otwórz plik w trybie zapisu i zapisz dane w formacie JSON
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(favourite, file, indent=4)

print(f"Favourite book/movie data has been written to {file_name}")
