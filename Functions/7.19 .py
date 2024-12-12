# Funkcja, która oblicza sumę powtarzających się cyfr w liczbie

def f(number):
    # Zamieniamy liczbę na string
    number_str = str(number)
    
    # Zmienna do przechowywania sumy powtarzających się cyfr
    repeated_sum = 0
    
    # Sprawdzamy każdą cyfrę 
    for digit in set(number_str):  # set usunie duplikaty

        # Jeśli dana cyfra występuje więcej niż raz, dodajemy jej wartość do sumy
        if number_str.count(digit) > 1:
            repeated_sum += int(digit) * number_str.count(digit)
    
    return repeated_sum

# Testowanie 
print(f(1027))        
print(f(230335))      
print(f(513553007))   
