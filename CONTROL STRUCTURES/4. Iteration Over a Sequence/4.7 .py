###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1, 11): # było samo n zmeiniamy na in
    if not i % 2 !=0 : #stawiamy warunek jeśli różnica jest różna od 0, kontynuuj 
        continue
    sum += i # przypisujemy zmienną i 

print(f'Sum of even numbers in the range <1,10> is {sum}')  # dodajemy f przed tekst i {sum}