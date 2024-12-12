# Definiujemy funkcję f, która przyjmuje ciąg znaków detector

def f(detector):
    count = 0  # licznik osób w pokoju

    # Przechodzimy przez każdy znak w ciągu
    for char in detector:
        if char == "+":
            count += 1  # Osoba wchodzi do pokoju
        elif char == "-":
            count -= 1  # Osoba wychodzi z pokoju
        
        # Jeśli w pokoju jest 3 lub więcej osób, zwrócimy True
        if count >= 3:
            return True
    
    # Jeśli mniej zwróci False
    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))
