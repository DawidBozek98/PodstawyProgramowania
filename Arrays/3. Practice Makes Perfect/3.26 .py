# Importowanie biblioteki do rysowania wykresów

import matplotlib.pyplot as plt
import math  

# Tworzenie listy wartości kąta od 0 do 360

x = []  # Lista na wartości kąta
y = []  # Lista na wartości sin(x)

# Obliczanie wartości kąta i sin(x)
for i in range(361):  # Zakres od 0 do 360
    x.append(i)  # Dodajemy kąt do listy x
    y.append(math.sin(math.radians(i)))  # Obliczamy sin(x) i dodajemy do listy y

# Rysowanie wykresu
plt.plot(x, y)  # Tworzymy wykres
plt.title("Wykres funkcji y = sin(x)")  # Tytuł wykresu
plt.xlabel("Kąt (stopnie)")  # Oś x
plt.ylabel("sin(x)")  # Oś y


plt.show()  # Wyświetlamy 
