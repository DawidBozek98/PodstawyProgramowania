# Enter car speed: 38
# Warning: invalid car speed!!

# Use the following variables in your program:

# car_speed
# speed_limit_min
# speed_limit_max


# Definiowanie zmiennych
speed_limit_min = 40 
speed_limit_max = 140 


car_speed = int(input("Enter car speed: "))

# sprawdzamy, czy prędkość mieści się w dozwolonym zakresie
if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
else:
    print("Car speed is within the valid range.")
