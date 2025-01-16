# Tworzenie słownika opisującego osobę
person = {
    "name": "Marek",  # String
    "surname": "Banach",  # String
    "age": 25,  # Integer
    "hobby": ["swimming", "excursions"],  # List
    "married": True,  # Boolean
    "phone": {"landline": "123444321", "mobile": "777888999"}  # Dictionary
}


print(f"Name: {person['name']}")


print(f"Hobby: {person['hobby']}")

# Wyświetlanie słownika
print("\nDictionary contents before updates:")
for key, value in person.items():
    print(f"{key}: {value}")

# Zmiana nazwiska na 'Nowak'
person["surname"] = "Nowak"

# Zmiana statusu małżeńskiego osoby
person["married"] = not person["married"]


person["gender"] = "male"

# Dodanie hobby 
person["hobby"].append("bicycle")

# Dodanie telefonu służbowego 
person["phone"]["work"] = "313131444"


print("\nDictionary contents after updates:")
for key, value in person.items():
    print(f"{key}: {value}")
