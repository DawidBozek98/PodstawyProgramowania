###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
index = 0 #indeks dla pętli while

# Count vowels in the text
# for char in text:
#     if char in vowels:
#         vowel_count += 1

while index < len(text):
    if text[index] in vowels: # Sprawdzamy, czy aktualny znak jest samogłoską
        vowel_count += 1 # Zwiększamy licznik samogłosek
    index += 1 # Przechodzimy do następnego znaku w tekście // przez złe wcięcię nie działało 


print(f"The number of vowels in the text is: {vowel_count}")