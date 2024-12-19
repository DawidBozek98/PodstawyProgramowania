import matplotlib.pyplot as plt

# Tworzenie list 
x = []  # Lista  x
y = []  # Lista y

# Generowanie wartości x w przedziale od -100 do 100
for n in range(-100, 101):  
    x.append(n)  # Dodajemy wartość n do listy x

# Obliczanie wartości y dla każdego x 
for n in x:  # Iterujemy przez wartości x
    y.append(n**2 - 3)  # Obliczamy z f i dodajemy wynik 


plt.plot(x, y)  # Tworzymy wykres z wartościami x i y
plt.title("Wykres funkcji f(x) = x^2 - 3")  # Dodanie tytułu do wykresu
plt.xlabel("x")  # Opis osi x
plt.ylabel("f(x)")  # Opis osi y


plt.show()  
