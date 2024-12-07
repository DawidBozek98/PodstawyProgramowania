# Szyfruje tekst za pomocą szyfru Cezara, przesuwając każdą literę w alfabecie o jedną pozycję w prawo
plain_text = 'The early bird catches the worm'
encrypted_text = ''

# Przechodzimy przez każdy znak w tekście
for char in plain_text:  
    if char.isalpha():  # Sprawdzamy, czy znak jest literą
        char_code = ord(char)  # Odczytujemy kod ASCII znaku (używamy ord())

        if char.islower():
            # Przesuwamy litery małe (od 'a' do 'z')
            new_char = chr((char_code - ord('a') + 1) % 26 + ord('a')) 
        elif char.isupper():
            # Przesuwamy litery wielkie (od 'A' do 'Z')
            new_char = chr((char_code - ord('A') + 1) % 26 + ord('A')) 
        
        encrypted_text += new_char  # Dodajemy zaszyfrowany znak do tekstu zaszyfrowanego
    else:
        encrypted_text += char  # Jeśli znak nie jest literą, dodajemy go do tekstu

# Drukujemy oryginalny i zaszyfrowany tekst
print(f'Oryginalny tekst: {plain_text}')
print(f'Zaszyfrowany tekst: {encrypted_text}')


#tutaj mocno kopałem w internecie
