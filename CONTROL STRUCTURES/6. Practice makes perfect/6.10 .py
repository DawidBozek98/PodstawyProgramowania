
# Enter the dog's age in human years: 15
# The dog's age in dog's years is 73 years.


human_years = int(input("Enter the dog's age in human years: "))

if human_years <= 2:
    dog_years = human_years * 10.5  # Pierwsze 2 lata psa to 10.5 ludzkiego roku każdy
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4  # Po 2 latach każdy kolejny rok to 4 lata ludzkie


print(f"The dog's age in dog's years is {int(dog_years)} years.")
