


# Program do tworzenia wzoru gwiazdek tutaj prostszy niż w java

# górna część piramidy
for i in range(1, 6):  # od 1 do 5
    print("* " * i)  

# dolna część piramidy
for i in range(4, 0, -1):  # Od 4 do 1 // musi być -1 gdy dawałem zero dolna część się nie drukowała
    print("* " * i)  # Drukowanie gwiazdek w odpowiedniej liczbie
