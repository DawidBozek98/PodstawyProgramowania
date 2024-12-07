# Most female names in Polish end with the letter "a". 
# Write a program that prints the name entered from the keyboard, 
# provided it is a female name. Sample result:

# Enter name: Anna
# Anna -- Polish female name

# Program sprawdzający, czy imię jest polskim imieniem żeńskim
name = input("Enter name: ")


if name.endswith("a"): #sprawdzamy czy imie konczy się na 'a'
    print(f"{name} -- Polish female name")
else:
    print(f"{name} -- Not a Polish female name")
