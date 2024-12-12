# Funkcja maskująca numer karty kredytowej
def hide(card_number):
    
    # Zwracamy pierwszy dwie cyfry, a następnie osiem gwiazdek, i cztery ostatnie cyfry
    return card_number[:2] + '*' * 8 + card_number[-4:]
