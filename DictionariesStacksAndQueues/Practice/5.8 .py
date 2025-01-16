prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

cart = {'juice': 3, 'bread': 1, 'milk': 2}

# kosz całkowity
total_cost = sum(prices[item] * cart.get(item, 0) for item in cart)

print("Total cost of the shopping cart:", round(total_cost, 2))
