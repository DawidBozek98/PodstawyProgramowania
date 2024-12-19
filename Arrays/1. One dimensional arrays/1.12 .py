# Kategorie wydatków
categories = ["Food", "Transport", "Rent", "Entertainment"]

# Wydatki 
expenses = [500, 150, 1000, 200]

# Obliczamy maksymalny wydatek
max_expense = max(expenses)

# Znajdujemy indeks kategorii z maksymalnym wydatkiem
max_expense_index = expenses.index(max_expense)


print("The most expensive expense category is:", categories[max_expense_index])
print("Amount:", max_expense)
