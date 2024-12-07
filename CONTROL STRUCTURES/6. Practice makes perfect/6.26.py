# Enter the PIN code: 2398
# Incorrect...
# Enter the PIN code: 0912
# Incorrect...
# Enter the PIN code: 7860
# Incorrect...
# Sorry, your payment card has been blocked.


correct_pin = "0805"

attempts = 3

# Pętla umożliwiająca trzy próby wprowadzenia PIN-u
while attempts > 0:
    entered_pin = input("Enter the PIN code: ")
     # Sprawdzenie, czy wprowadzony PIN jest poprawny
    if entered_pin == correct_pin:
        print("PIN code is correct.")
        break
    else:
        # Zmniejszamy liczbę prób
        attempts -= 1
        if attempts > 0:
            print("Incorrect... You have", attempts, "attempt(s) left.")
        else:
            print("Sorry, your payment card has been blocked.")
