import re  # re wyrażenia regularne

def count_vowels(text):
    # Szukamy samogłoske w tekście małe i duże
    vowels = re.findall(r'[aeiouAEIOU]', text)
    # Zwracamy liczbę samogłosek
    return len(vowels)


text = input("Enter some text: ")

# Liczymy samogłoski w tym tekście
vowel_count = count_vowels(text)

print("Number of vowels:", vowel_count)
