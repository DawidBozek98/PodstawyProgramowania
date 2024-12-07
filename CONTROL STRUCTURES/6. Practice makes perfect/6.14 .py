# facebook = True
# twitter = False
# instagram = True
# You are a good influencer!

# Zmienna logiczna dla poszczególnych mediów społecznościowych
facebook = True
twitter = False
instagram = True


active_accounts = sum([facebook, twitter, instagram]) #sprawdzamy tutaj ile z tych kont jest ustawionych na True

# warunek czy ilość kont jest >= 2
if active_accounts >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")
