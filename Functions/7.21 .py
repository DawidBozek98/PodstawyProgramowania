# Funkcja, która oblicza różnicę między największą a najmniejszą liczbą

def f(number1, number2, number3):

    # Zbieramy liczby w liście
    numbers = [number1, number2, number3]
    
    # Znajdujemy największą liczbę w liście
    largest = max(numbers)
    
    # Znajdujemy najmniejszą liczbę w liście
    smallest = min(numbers)
    
    # Obliczamy różnicę między największą a najmniejszą liczbą
    difference = largest - smallest
    
    return difference


print(f(7, 4, 9))  # Zwróci 5
print(f(2, 12, 8)) # Zwróci 10
