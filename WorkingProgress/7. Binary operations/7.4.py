print('7.4')
#Enter tree circumference in cm: 120 
#Tree can be cut down: False

circumference = float(input('Enter circumference in cm: '))

pi = 3.1416 #przybliżona wartość liczby pi

diameter = circumference / pi #liczymy średnicę dzieląc obówd przez pi

legall_cut = diameter >= 50 #porównanie czy średnica jest większa lub równa 50cm

print(f'Tree can be cut down: {legall_cut}')
