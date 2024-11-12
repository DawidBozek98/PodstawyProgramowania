print(6.9)
print()
###
# Character code conversion
#67, 111, 111, 108, 33
print(chr(67),chr(111),chr(111),chr(108),chr(33))
# C o o l !
print()

print(6.10)
print()


###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in capital letters: ', movie.upper())

# print title in small letters
print('Title in small letters: ', movie.lower())
# print how many times the vowel "e" appears in the title
print('Number of times "e" appears: ', movie.count('e'))

# print where in the text is the word "Lord"
print('Position of the word "Lord": ', movie.find('Lord'))

# print where in the text is the word "dragon"
print('Position of the word "dragon": ', movie.find('dragon')) #pokazuje wartość -1, nie ma takiego słowa w tym zacnym tytule