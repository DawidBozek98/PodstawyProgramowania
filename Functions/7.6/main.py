import credit_card

card_number = "5290312400019022"

# Maskujemy numer karty
masked_card = credit_card.hide(card_number)

print(f"Masked card number: {masked_card}")
