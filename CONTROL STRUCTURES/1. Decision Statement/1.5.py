###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input('Enter number of properly performed tasks: '))
test_passed = False #Jest to flaga, która wskazuje czy zaliczone czy nie

if tasks_ok >= total_tasks / 2 :
    test_passed = True #zmiana flagi na true

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')