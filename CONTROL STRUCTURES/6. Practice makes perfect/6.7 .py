# Write a program that asks the user for their age and then checks which age 
# group they belong to:

# Child: under 13
# Teen: 13 to 19
# Adult: 20 to 64
# Senior: 65 or older

age = int(input("Enter your age: "))

# Sprawdzamy, do jakiej grupy wiekowej należy użytkownik
if age < 13:
    age_group = "Child"
elif 13 <= age <= 19:
    age_group = "Teen"
elif 20 <= age <= 64:
    age_group = "Adult"
else:                       #else zawsze kończy i musi być " : "
    age_group = "Senior"


print(f"You belong to the {age_group} group.") #wyświetlamy grupę
