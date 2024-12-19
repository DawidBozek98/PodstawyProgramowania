# Wyniki testu (True - poprawna odpowiedź, False - błędna odpowiedź)
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# Obliczamy liczbę pytań w teście
question_number = len(test_results)

# Obliczamy liczbę poprawnych odpowiedzi
correct_answers = 0
for answer in test_results:
    if answer:  
        correct_answers += 1

# Obliczamy liczbę błędnych odpowiedzi
incorrect_answers = question_number - correct_answers

# Obliczamy procent poprawnych odpowiedzi
percentage_correct = (correct_answers / question_number) * 100


print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers:', f"{percentage_correct:.2f}%")
