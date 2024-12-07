# Enter EAN-13 article number: 5901230094938
# Article number is correct
# Article manufactured in Poland



ean_number = input("Enter EAN-13 article number: ")

# sprawdzamy, czy numer składa się z dokładnie 13 cyfr
if len(ean_number) == 13 and ean_number.isdigit():
    print("Article number is correct")
    
    # sprawdzamy, czy numer zaczyna się od "590" (produkty wyprodukowane w Polsce)
    if ean_number.startswith("590"):
        print("Article manufactured in Poland")
else:
    print("Invalid article number")
