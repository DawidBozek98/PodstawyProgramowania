
import count_letter

# Tekst
text = "You never get a second chance to make a first impression"

# Litera, której wystąpienia chcemy policzyć
letter = 'e'

# Używamy funkcji count_letter
count = count_letter.count_letter(text, letter)


print(f"The number of letter '{letter}': {count}")
