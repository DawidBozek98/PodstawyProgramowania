#Enter number: 125
#Binary number: 0b1111101
#Hexadecimal number: 0x7d


decimal_number = int(input('Enter an intiger')) #podajemy liczbę całkowitą
binary_number = bin(decimal_number)[2:] #usuwamy początek liczby 0b 
hexadecimal_number = hex(decimal_number)[2:].upper()#usuwamy prefiks 0x i zmieniamy na duże litery

print(f'Binary representation: {binary_number}')
print(f'Hexadecimal representation: {hexadecimal_number}')