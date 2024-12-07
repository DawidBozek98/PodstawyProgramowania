###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') ) #wprowadzamy z klawiatury dane o prędkości

if car_speed > speed_limit :  #prównujemy pola jest to bool
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')