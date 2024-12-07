###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = float(input("Enter percent of bonus: "))  #ułatwienie do testu
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'  #flaga na true

if is_bonus == "N" :
    print(f'You get only a basic salary {basic_salary}')
else:
    total_salary = (basic_salary * bonus) + basic_salary #obliczamy całkowitą premię
    print(f'Basic salary: {basic_salary}')
    print(f'Bonus included? {is_bonus}')
    print(f'Total salary: {total_salary}')