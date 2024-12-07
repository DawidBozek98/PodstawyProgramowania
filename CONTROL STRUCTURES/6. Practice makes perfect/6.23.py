

# Program do generowania tabeli mnożenia


number = int(input("Enter number: "))

# Pętla do tworzenia tabeli mnożenia od 1 do 10
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
