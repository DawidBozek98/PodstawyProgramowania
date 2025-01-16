
paragraph = "cat dog mouse cat rat cat mouse"

# do przechowania liczby wystąpień słów
word_count = {}

# paragraf na słowa
words = paragraph.split()


for word in words:
    # zwiększa licznik
    if word in word_count:
        word_count[word] += 1
    else:
        # Jeśli słowo nie występuje w słowniku, dodaje je z liczbą 1
        word_count[word] = 1
print("Word count:")
for word, count in word_count.items():
    print(f"{word}: {count}")
