#Enter vehicle speed: 158
#Speed is valid: False

vehicle_speed = int(input('Enter vehicle speed in km/h: '))
correct_speed = 40 <= vehicle_speed <= 140 #wydzielamy okno prawidłowych wartości
print(f'Speed is valid: {correct_speed}')