# Importowanie wymaganej biblioteki do rysowania wykresów

import matplotlib.pyplot as plt

# Definiowanie punktów na osi X i Y
xpoints = [1, 8]  
ypoints = [3, 10]  

# Rysowanie linii między punktami (1, 3) a (8, 10)
plt.plot(xpoints, ypoints)  # Funkcja rysuje linię 


plt.show()  # Pokazuje wykres 


#pip install matplotlib w konsoli